from numpy import outer
from telethon.sync import TelegramClient, events
import datetime
from telethon.sessions import StringSession
import re
from mapping import MAPPING


api_id = 111111
api_hash = '1111111111'
SOURCE_CHANNEL = ['betfront_bot']

client = TelegramClient('test', api_id, api_hash)
client.start()
phone = "+7911111111"
chats = ['betfront_bot']

def get_teams():
    for chat in chats:
        with TelegramClient('exparibot', api_id, api_hash) as client:
            for message in client.iter_messages(chat, offset_date=datetime.date.fromisoformat('2022-08-01') , reverse=True):
                # написать try/except (видимо для search)
                # print(message.to_dict()['message'])
                res = re.search(r".title=(.*)descr", str(message))
                game = res.group(1)
                game = game.split('. ')
                try:
                    # print(game[2].split(' - '))
                    away_team = game[2].split(' - ')
                    home_team = away_team[0]
                    # print(home_team)
                    away_team = away_team[1].split(' (')
                    # print(home_team, '-', away_team[0])
                    outcome = away_team[1].split(' ')
                    outcome = outcome[1]
                    # print(outcome)
                except:
                    pass    
    return home_team, away_team[0], outcome

def transfer_mapping(home_team, away_team, outcome):
    '''Названия команд из expari (то есть линии Pinnacle) переводим в названия команд в Orbitexch через MAPPING'''
    try:
        home_team_orbit = MAPPING[home_team]
        away_team_orbit = MAPPING[away_team]
        outcome_orbit = outcome
        game_name_orbit = f'{home_team_orbit} v {away_team_orbit}'
        print(game_name_orbit, outcome_orbit)
        return game_name_orbit, outcome_orbit
    except:
        print('Ошибка в mapping')

home_team_pin, away_team_pin, outcome_pin = get_teams()
print(home_team_pin, away_team_pin, outcome_pin)
game_name_orbit = transfer_mapping(home_team_pin, away_team_pin, outcome_pin)
print(game_name_orbit[0])

# Обработчик новых сообщений
# @client.on(events.NewMessage(chats=SOURCE_CHANNEL))
# async def handler_new_message(event):
#     try:
#         print(event.message)
#         # отправим сообщение в наш канал
#         # await client.send_message(TARGET_CHANNEL, event.message)
#         # либо вместо переотправки можно репостнуть:
#         # await client.forward_messages(TARGET_CHANNEL, event.message)
#     except Exception as e:
#         print(e)


# client.run_until_disconnected()