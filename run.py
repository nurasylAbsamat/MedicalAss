from python_webex.v1.Bot import Bot
from python_webex import webhook

bot = Bot()

bot.create_webhook(
    name="quickstart_webhook", target_url="https://8604df6b.ngrok.io", resource="messages", event="created"
)

@bot.on_hears("hi")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="Hi! How is your health? What is bothering you?")

@bot.on_hears("*")
def default_response(room_id=None):
    return bot.send_message(room_id=room_id, text="Sorry, could not understand that")


# make the webhook know the bot to be listening for, and we are done
webhook.bot = bot

if __name__ == "__main__":
    webhook.app.run(debug=True)  