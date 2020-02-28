from python_webex.v1.Bot import Bot
from python_webex import webhook
import json
from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.inputs import Text, Number
from pyadaptivecards.components import TextBlock
from pyadaptivecards.actions import Submit
# bot = Bot()
#
# bot.create_webhook(
#     name="quickstart_webhook", target_url="https://8604df6b.ngrok.io", resource="messages", event="created"
# )
#
# @bot.on_hears("hi")
# def greet_back(room_id=None):
#
#     return bot.send_message(room_id=room_id, text="Hi! How is your health? What is bothering you?")
#
# @bot.on_hears("*")
# def default_response(room_id=None):
#     return bot.send_message(room_id=room_id, text="Sorry, could not understand that")


# make the webhook know the bot to be listening for, and we are done
# webhook.bot = bot
greeting = TextBlock("Hey hello there! I am a adaptive card")
first_name = Text('first_name', placeholder="First Name")
age = Number('age', placeholder="Age")

submit = Submit(title="Send me!")

card = AdaptiveCard(body=[greeting, first_name, age], actions=[submit])
card_json = json.loads(card.to_json(pretty=True))
print(card_json['actions'][0]['title'])


