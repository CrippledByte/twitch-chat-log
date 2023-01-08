# twitch-chat-log
Logs Twitch channel messages to file

## Installation

### Linux
```sh
mkdir env
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### Windows
```bat
mkdir env
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Usage
To run chatlog.py, you will need to provide an OAuth access token with the chat_login scope. ~~You can reference an authentication sample to accomplish this, or~~ simply use the [Twitch Chat OAuth Password Generator](http://twitchapps.com/tmi/).

```sh
$ python chatlog.py <username> <oath:token> <channel>
```
* Username - The username of the chatbot
* Token - Your OAuth Token
* Channel - The channel your bot will connect to

When this script is running, messages are stored in files with the format `channelname.log.2023-01-01_00-00-00+0000`. A new file will be created at midnight UTC every day.
