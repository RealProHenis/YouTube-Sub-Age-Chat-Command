# YouTube Sub Age Command (Streamlabs Chatbot Script)

A chat command for YouTube streamers (who use Streamlabs Chatbot) that allows viewers to type !subage in live chat, and the bot will respond with the date & time that the user subscribed to the streamer's channel

## Streamer Requirements

Must have Python 2.7.13 installed on the same computer that's running Streamlabs Chatbot and have the correct directory set in Streamlabs Chatbot Script Settings 

Learn more: https://streamlabs.com/content-hub/post/chatbot-scripts-desktop

## Viewer Requirements

Viewers MUST have their YouTube subscription privacy settings set public in order for Streamlabs Chatbot to retrieve their subscription date. They can do this by following these steps:
1. Sign in to YouTube on a computer
2. In the top right, click your profile picture
3. Click Settings 
4. In the left Menu, select Privacy
5. Turn off "Keep all my subscriptions private"

## How To Setup

1. Download ZIP (click the "Code" drop down, and then click "Download ZIP")
2. Open StreamLabs Chatbot, go to the Scripts tab, click the Import button in the upper right, and choose the ZIP file you just downloaded
    - You can also install the script manually by extracting the ZIP file to %AppData%\Roaming\Streamlabs\Streamlabs Chatbot\Services\Scripts
3. Once the script has successfully loaded, click on the script in Streamlabs Chatbot and you should see the script settings appear
    - Here you can change the trigger command, permission level, user cooldown, and time format of the command response
5. Get your YouTube channel ID from here: https://commentpicker.com/youtube-channel-id.php and enter it into the Streamer Channel ID field of the script settings in Streamlabs Chatbot
6. Get a YouTube API Key: (a YouTube Data v3 API Key is required to check a user's subscription status)
    - Go to https://console.cloud.google.com
    - Click "Select a project" dropdown in the upper left, then click "New Project" (name the project whatever you want)
    - Wait for the project to be created, then click "Select Project"
    - On the left sidebar, hover over "APIs & Services", then click "Enabled APIs & Services"
    - Click "Enable APIs & Services"
    - Search "youtube" and click "YouTube Data API v3"
    - Click "Enable" and wait for the API to be enabled
    - Click the "Credentials" tab on the left sidebar (under APIs & Services)
    - Click "Create Credentials" at the top, then click "API key"
    - Once your API Key is created, copy it and enter it into the YouTube API Key field of the YouTube Sub Age script settings in Streamlabs Chatbot
7. Choose a time format to display the user's subscription date/time
    - If you want to use a different time format, submit an issue on this GitHub and I'll update when I can
8. Click "Save Settings" at the bottom of the script settings
9. Make sure the command is enabled!
10. You're all set!
