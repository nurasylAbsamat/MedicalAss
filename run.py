from python_webex.v1.Bot import Bot
from python_webex import webhook
import json
import requests
from python_webex.v1.Bot import Bot
from webexteamssdk import WebexTeamsAPI

bot = Bot()
api = WebexTeamsAPI(access_token='MTk1OTJkN2MtZmU0Mi00YjI4LWE4OGYtODJiMWM3ZWI3MDk2YWE2MzUxMWMtZTYx_PF84_consumer')

all_rooms_response = bot.get_all_rooms()
all_rooms = all_rooms_response.json()

bot.create_webhook(
    name="quickstart_webhook", target_url="https://66f567f8.ngrok.io", resource="messages", event="created"
)

@bot.on_hears("1")
def greet_back1(room_id=None):
    return bot.send_message(room_id=room_id, text="Write which of these bothers you: \nHead?\nStomach?\nHeat?\nThroat?\nHeart?\nCold?\nStress?")

@bot.on_hears("2")
def greet_back2(room_id=None):
    return bot.send_message(room_id=room_id, text="Write which of these bothers you: \nHead?\nStomach?\nHeat?\nThroat?\nHeart?\nCold?\nStress?")

@bot.on_hears("3")
def greet_back3(room_id=None):
    return bot.send_message(room_id=room_id, text="Write which of these bothers you: \nHead?\nStomach?\nHeat?\nThroat?\nHeart?\nCold?\nStress?")
@bot.on_hears("4")
def greet_back4(room_id=None):
    #return (bot.get_message_details(message_id=None))
    #return bot.get_message_details(bot.get_message_details(message_id=None))
    room_details_response = bot.get_room_details(room_id=room_id)
    room_details = room_details_response.json()


    me = api.people.get((room_details["creatorId"])).emails[0]
    #api.rooms.delete(room_id)

    demo_room = api.rooms.create('Contact with Doctor')
    email_addresses = [me, "miras.shakh@gmail.com"]
    for email in email_addresses:
        api.memberships.create(demo_room.id, personEmail=email)
    api.messages.create(demo_room.id, text="Welcome to the room!",
                        files=["https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"])


@bot.on_hears("Head")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="It can be assumed colds, acute respiratory viral infection\nAcute respiratory viral infection. This is one of the most common infectious diseases (we all know the diagnosis of ARI). Its prevalence is epidemic. Infection occurs from a sick person by airborne droplets.\nManifestations: chills suddenly appear, body temperature rises quickly, more often to high (38-40 ° С). A general malaise is growing - weakness, 'fatigue', body aches. In acute respiratory infections, headache is felt, as a rule, in the frontal region, with eye movements. Against the background of high temperature, nausea, vomiting, dizziness are possible. The skin is hot but moist to the touch. During the day, nasal congestion, runny nose, lacrimation, sore throat, hoarseness, dry, excruciating cough appear. The pharynx is bright red.\nTreatment is carried out by a general practitioner, an infectious disease specialist. Before that, you can take antipyretic, anti-inflammatory drugs, a heavy drink is indicated.")
@bot.on_hears("Cold")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="It can be assumed colds, acute respiratory viral infection\nAcute respiratory viral infection. This is one of the most common infectious diseases (we all know the diagnosis of ARI). Its prevalence is epidemic. Infection occurs from a sick person by airborne droplets.\nManifestations: chills suddenly appear, body temperature rises quickly, more often to high (38-40 ° С). A general malaise is growing - weakness, 'fatigue', body aches. In acute respiratory infections, headache is felt, as a rule, in the frontal region, with eye movements. Against the background of high temperature, nausea, vomiting, dizziness are possible. The skin is hot but moist to the touch. During the day, nasal congestion, runny nose, lacrimation, sore throat, hoarseness, dry, excruciating cough appear. The pharynx is bright red.\nTreatment is carried out by a general practitioner, an infectious disease specialist. Before that, you can take antipyretic, anti-inflammatory drugs, a heavy drink is indicated.")
@bot.on_hears("Throat")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="The general rule for any cold is to drink enough fluids. This reduces intoxication and accelerates the elimination of destroyed viruses. To relieve a \N{grinning face}sore throat, drink both warm and cool drinks more often.With severe discomfort - when your working capacity is significantly reduced against the background of the disease - it is worth using drugs with anesthetic and anti-inflammatory effect, such as acetaminophen (paracetamol, panadol), ibuprofen (nurofen) or aspirin (the latter can be taken from the age of 18). It is also important to maintain sufficient humidity in the room (at least 50%), for example, with the help of air - a device that can clean and moisten the air mass, ensuring its constant circulation - or by putting a wet towel on the battery, although in this case you can only humidify the air, but not clean it.")

@bot.on_hears("Heart")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="This information about Heart &#128147; : \nThe main and basic rule is to ensure complete peace immediately. Sit or lie down, find a position in which heart pain will be less noticeable.It is important to provide fresh air to saturate the body with oxygen. Go outside or open a window. If the pain in the heart does not stop, you should take an anesthetic. The most available: Paracetamol, Analgin, Nimesil or Ibuprofen. Take aspirin Firstly, he anesthetizes. Secondly, the drug dilutes the blood (reduces its coagulation). This improves blood flow and can relieve Chest pain: First aid condition in cases where chest pain is still associated with problems in the cardiovascular system. Attention! In no case do you take aspirin if you are allergic to it or you suffer from diseases associated with low blood clotting. Drink warm tea. Or another warm drink. This recommendation may work if chest pain occurs soon after eating.")

@bot.on_hears("Stomach")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="do not take medicines for nausea and vomiting. To prevent dehydration, drink plenty of fluids without dyes and gases. 2-3 days - hunger. After 2-3 days, when vomiting stops, you can eat a light broth, boiled potatoes or rice. Have a rest, adhere to bed rest, at the first opportunity try to take a nap. Rotavirus infection is a viral disease of the digestive tract, usually resolves in a few days. If pain or vomiting intensifies, call a doctor. Attention! If all these manifestations are accompanied by problems with vision (double in the eyes), problems with speech and speed of reactions, this may indicate severe poisoning - a condition that directly threatens life.")

@bot.on_hears("Stress")
def greet_back(room_id=None):
    return bot.send_message(room_id=room_id, text="Fluid is really needed for colds. Dried fruit compote or warm tea helps to cope with unpleasant symptoms. You should drink 3-5 cups a day more than when you are healthy. Respiratory gymnastics is especially indicated for people who, due to their personality traits, react extremely emotionally to stress, thereby exacerbating the situation. Five to ten calm breaths can protect you from rash acts, and the habit of breathing regularly through one of the special programs that require only a few minutes a day helps fight irritability or anxiety attacks.")
@bot.on_hears("*")
def default_response(room_id=None):
    room_details_response = bot.get_room_details(room_id=room_id)
    room_details = room_details_response.json()
    print(room_details['creatorId'])
    print(api.people.get(room_details).emails)
    name = room_details['title']
    return bot.send_message(room_id=room_id, text="Hello {0},\n I need an assessment of your condition from 1 to 5, please write your answer! ".format(name))

# make the webhook know the bot to be listening for, and we are done
webhook.bot = bot



#
#
#
# # Find all rooms that have 'webexteamssdk Demo' in their title
#
# # Delete all of the demo rooms
# for room in demo_rooms:
#
# # Create a new demo room
#
# # Add people to the new demo room
#
# # Post a message to the new room, and upload a file
#

webhook.app.run(debug=True)
