from datetime import datetime
import json
import random
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_WEBHOOK = os.getenv('BOT_WEBHOOK')
OKTOBERFEST_DATE = os.getenv('OKTOBERFEST_DATE')
DATE_FORMAT= os.getenv('DATE_FORMAT')
BOT_USERNAME = os.getenv('BOT_USERNAME')
BOT_AVATAR = os.getenv('BOT_AVATAR')

def get_date_difference():
    date_now = datetime.now()
    oktoberfest = datetime.strptime(OKTOBERFEST_DATE, DATE_FORMAT)
    diff_date = oktoberfest - date_now
    days = diff_date.days
    hours = diff_date.seconds / 3600
    minutes = (diff_date.seconds % 3600) / 60
    return (list(map(round,[days, hours, minutes])))

def get_music():
    with open('musics.json', 'r') as json_file:
        json_data = json.load(json_file)
    music = random.choice(json_data)
    return music['music'] 

def get_message():
    with open('messages.json', 'r') as json_file:
        json_data = json.load(json_file)
    message = random.choice(json_data)
    return message['message'] 

def main():
    days_remaning, hours_remaning, minutes_remaning = get_date_difference()
    message = get_message()
    music = get_music()
    data = {'content': message.format(days = round(days_remaning), 
                               hours = round(hours_remaning),
                                minutes= round(minutes_remaning))
                                +'\n\n **A musica do dia é** ' + music,
            'username': BOT_USERNAME,
            'avatar_url': BOT_AVATAR
            }
    print(data)
    x = requests.post(BOT_WEBHOOK, data = data)
    print(x)

if __name__ == '__main__':
    main()