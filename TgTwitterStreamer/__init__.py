# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterStreamer
# GNU General Public License v3.0


from Configs import Var

REPO_LINK = "https://twitter.com/bankerdoge"


CUSTOM_FORMAT = """🚨 NEW **[{SENDER}]({SENDER_PROFILE})** TWEET ALERT 🚨:

{TWEET_TEXT}

• **[Official Twitter]({_REPO_LINK})**"""


if not Var.CUSTOM_TEXT:
    Var.CUSTOM_TEXT = CUSTOM_FORMAT
