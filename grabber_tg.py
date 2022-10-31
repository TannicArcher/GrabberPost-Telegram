# слито в @end_software
from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, sync
from telethon import TelegramClient, events, sync

# слито в @end_software

api_id = 123456 # ваши данные, брать с my.telegram.org
api_hash = "ada12245jsfo5o2525o6o36" # ваши данные, брать с my.telegram.org

# слито в @end_software

client = TelegramClient("Test", api_id, api_hash) # логинимся
client.start() # старт клиента
@client.on(events.NewMessage(chats=["test1", 'test2'])) # список каналов, откуда будем брать посты
async def normal_handler(event):
if isinstance(event.chat, types.Channel):
username = event.chat.username
rdy = "@" + str(username) # получаем юзернейм канала, откуда забрали пост
await client.send_message("https://t.me/joinchat/AAAAAE1t242", rdy) # будет отправлять инфу, о том, с какого канала спизжен пост
await client.send_message("https://t.me/joinchat/AAAAAE1t242", event.message) # отправка поста в канал
client.run_until_disconnected()
# слито в @end_software
