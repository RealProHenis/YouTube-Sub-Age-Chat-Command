import os
import sys
import json
import datetime
import codecs

sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#Import your Settings class
from Settings_Module import MySettings

ScriptName = "YouTube Sub Age"
Website = "https://youtube.com/prohenis"
Description = "Type !subage in YouTube chat and Streamlabs Chatbot will return the date & time the user subscribed to the channel. (only if the user has their YouTube subscriptions public)"
Creator = "ProHenis"
Version = "1.0.0.0"

settings = {}

def Init():
    global settings
    work_dir = os.path.dirname(__file__)

    with codecs.open(os.path.join(work_dir, "settings.json"), encoding='utf-8-sig') as json_file:
        settings = json.load(json_file, encoding='utf-8-sig')
    return


def Execute(data):
    
    UserPerm = Parent.HasPermission(data.User, settings["Permission"], settings["Command"])
    
    if data.GetParam(0) != settings["Command"]:
        return
    if Parent.IsOnUserCooldown(ScriptName, settings["Command"], data.User):
        log(data.UserName + " - FAILED: user still has cooldown")
        return
    if UserPerm != 1:
        log(data.UserName + " - FAILED: user does not have permission")
        return

    chatterUsername = data.UserName
    chatterChannelID = data.User

    headers = {}
    request = Parent.GetRequest("https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet%2CcontentDetails&forChannelId=" + settings["streamerChannelID"] + "&channelId=" + chatterChannelID + "&key=" + settings["youtubeAPIKey"], headers)
    
    request_json = json.loads(request)

    # Output the API request to a text file in AppData\Roaming\Streamlabs\Streamlabs Chatbot for debugging (remove # before lines 55 & 56 to enable)
    #with open("youtubesubage_api_output.txt", "w") as file:
    #    file.write(request)

    if "error" in request_json and request_json["error"] == "Forbidden":
        Parent.SendStreamMessage("@" + chatterUsername + " subscription privacy is set to private. Change it to public here: https://www.youtube.com/account_privacy")
        log(data.UserName + " - FAILED: user subscriptions set to private")
    elif 'totalResults' in request_json['response'] and json.loads(request_json['response'])['pageInfo']['totalResults'] == 0:
        Parent.SendStreamMessage("@" + chatterUsername + " is not subscribed to the channel")
        log(data.UserName + " - FAILED: user not subscribed to the channel")
    elif 'publishedAt' in request_json['response']:
        items = json.loads(request_json["response"])["items"]
        published_at = items[0]["snippet"]["publishedAt"]

        # Handles new & old time formats
        if '.' in published_at:
            timestamp = datetime.datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            timestamp = datetime.datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")

        time_format = settings["timeFormat"]

        if time_format == "Name of Month-Day-Year":
            formatted_time = timestamp.strftime("%B %d, %Y")
        if time_format == "Name of Month-Day-Year 12hr Clock":
            formatted_time = timestamp.strftime("%B %d, %Y %I:%M %p UTC")
        if time_format == "Name of Month-Day-Year 12hr Clock w/ Seconds":
            formatted_time = timestamp.strftime("%B %d, %Y %I:%M:%S %p UTC")
        if time_format == "Name of Month-Day-Year 24hr Clock":
            formatted_time = timestamp.strftime("%B %d, %Y %H:%M UTC")
        if time_format == "Name of Month-Day-Year 24hr Clock w/ Seconds":
            formatted_time = timestamp.strftime("%B %d, %Y %H:%M:%S UTC")
        if time_format == "Month-Day-Year":
            formatted_time = timestamp.strftime("%m-%d-%Y")
        if time_format == "Month-Day-Year 12hr Clock":
            formatted_time = timestamp.strftime("%m-%d-%Y %I:%M %p UTC")
        if time_format == "Month-Day-Year 12hr Clock w/ Seconds":
            formatted_time = timestamp.strftime("%m-%d-%Y %I:%M:%S %p UTC")
        if time_format == "Month-Day-Year 24hr Clock":
            formatted_time = timestamp.strftime("%m-%d-%Y %H:%M UTC")
        if time_format == "Month-Day-Year 24hr Clock w/ Seconds":
            formatted_time = timestamp.strftime("%m-%d-%Y %H:%M:%S UTC")
        if time_format == "Day-Month-Year":
            formatted_time = timestamp.strftime("%d-%m-%Y")
        if time_format == "Day-Month-Year 12hr Clock":
            formatted_time = timestamp.strftime("%d-%m-%Y %I:%M %p UTC")
        if time_format == "Day-Month-Year 12hr Clock w/ Seconds":
            formatted_time = timestamp.strftime("%d-%m-%Y %I:%M:%S %p UTC")
        if time_format == "Day-Month-Year 24hr Clock":
            formatted_time = timestamp.strftime("%d-%m-%Y %H:%M UTC")
        if time_format == "Day-Month-Year 24hr Clock w/ Seconds":
            formatted_time = timestamp.strftime("%d-%m-%Y %H:%M:%S UTC")
        
        Parent.SendStreamMessage("@" + chatterUsername + " subscribed on " + formatted_time)
        log(data.UserName + " - SUCCESS: posted time in chat")
        Parent.AddUserCooldown(ScriptName, settings["Command"], data.User, settings["userCooldown"])
    
    return

def log(message):
    Parent.Log(settings["Command"], message)
    return

def Tick():
    return
