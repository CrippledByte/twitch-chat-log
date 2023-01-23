'''
From: https://github.com/twitchdev/chatbot-python-sample/blob/main/chatbot.py

2021-12-07
Modified to log Twitch channel chat messages.
'''

'''
Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
'''

import sys
import irc.bot
import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(level=logging.INFO)

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.token = token
        self.channel = channel

        # Set up logger
        self.logger = logging.getLogger('chatlogger')
        logname = "{}.log".format(channel.replace('#', '')) # create file for channel, remove leading '#' from channel name
        handler = TimedRotatingFileHandler(logname, when="midnight", interval=1, utc=True) # create a new file every day
        handler.suffix = "%Y-%m-%d_%H-%M-%S%z" # add date and time to filename
        self.logger.addHandler(handler)

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, username)

    def on_welcome(self, c, e):
        print('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        self.logger.info(e) # log events to file

    def on_action(self, c, e):
        # /me
        self.logger.info(e)

    def on_clearchat(self, c, e):
        # /clear
        # /timeout
        # /ban
        self.logger.info(e)

def main():
    if len(sys.argv) != 4:
        print("Usage: python chatlog.py <username> <oath:token> <channel>")
        sys.exit(1)

    username    = sys.argv[1]
    token       = sys.argv[2] # 'oath:token'
    channel     = '#' + sys.argv[3]

    bot = TwitchBot(username, token, channel)
    bot.start()

if __name__ == "__main__":
    main()
