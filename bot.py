from pymongo import *
import requests
from bs4 import BeautifulSoup
import re
import json
import humanize
from asyncio import events
import telebot
from telebot import types
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
import requests
import re
from bs4 import BeautifulSoup
from pymongo import *
import base64
import random

client = MongoClient("mongodb+srv://notpointbreak:Password246M@cluster0.gzxc2sc.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('bifrost')
links = db.gdtot

TOKEN = '6530908059:AAEsMAx3YoJoA04eCcfaLRskXOFtFkuUvqo'

bot = telebot.TeleBot(TOKEN)

img_link = ['https://i.pinimg.com/originals/2b/38/1e/2b381e29d6c14418cf104d07803403d5.jpg',
 'https://i.pinimg.com/originals/13/c5/72/13c572b686edd84fa16c0054da9c323d.jpg',
 'https://i.pinimg.com/originals/1f/bc/df/1fbcdf26cffe1f066edb2e4efed54d4a.jpg',
 'https://i.pinimg.com/originals/67/b4/c6/67b4c6e04a2c686076847241cd0cb88c.jpg',
 'https://i.pinimg.com/originals/d5/30/c9/d530c920c3a69d82744ea9586e2d8f38.jpg',
 'https://themighty.com/wp-content/uploads/2019/09/emotionalclub.png',
 'https://i.pinimg.com/originals/78/b1/30/78b13064c660fe2ebbe5224538f82d32.jpg',
 'https://i.pinimg.com/originals/7a/35/7b/7a357ba8fcb4d458e527a77b5af62a1a.jpg',
 'https://i.pinimg.com/originals/f7/7f/81/f77f811f65662f913ab0a727dfa5205a.jpg',
 'https://i.pinimg.com/originals/f7/7f/81/f77f811f65662f913ab0a727dfa5205a.jpg',
 'https://i.pinimg.com/originals/3b/8a/a7/3b8aa74a49e606ae1eaa46a25562dab1.jpg',
 'https://www.yatzer.com/sites/default/files/media/slideshow/15_s_daily_bat_stood_up_-photography_sebastian_magnani_yatzer.jpg',
 'https://i.pinimg.com/originals/fc/3a/da/fc3ada4114d5068067708a7d61e6354f.jpg',
 'http://www.teamjimmyjoe.com/wp-content/uploads/2016/01/street-sign-your-life-is-a-joke.jpg',
 'https://i.pinimg.com/originals/95/fe/9f/95fe9f2289ff1b5132320d94e8a7cd50.jpg',
 'https://i.pinimg.com/originals/71/94/58/71945842e6985f179772c11a65bfb3c9.jpg',
 'https://i.pinimg.com/originals/55/f0/05/55f0052e278d1f8615b42df235ff8836.jpg',
 'https://i.pinimg.com/originals/28/79/5c/28795cb77cc3fe6af94d8a73e023d1b3.jpg',
 'https://i.pinimg.com/originals/99/c8/13/99c813da11220eef9b1fcae3df9a5142.jpg',
 'https://i.pinimg.com/originals/c5/95/f1/c595f1e447ceec4cb09633cd915acf4c.jpg',
 'https://i.pinimg.com/originals/f6/bf/bc/f6bfbc8fdb2a5b3de5dc597c948ff072.jpg',
 'https://i.pinimg.com/originals/33/a8/cd/33a8cd881caa3774dc22f15cf92dc81c.jpg',
 'https://i.pinimg.com/originals/9e/7f/d9/9e7fd9fa9aba415f1b20b80ff112ca8a.jpg',
 'https://i.pinimg.com/originals/6d/1c/d5/6d1cd5db612dbfe80b894dacf137149a.jpg',
 'https://i.pinimg.com/originals/9d/b1/26/9db126488032b179abe1cb0e49daba8a.jpg',
 'https://i.pinimg.com/originals/06/12/4f/06124f2a2f848583488e74dbda1f4973.jpg',
 'https://i.pinimg.com/originals/51/f7/08/51f7086485a0be22204bfe1e29d03a59.jpg',
 'https://i.pinimg.com/originals/be/1d/b5/be1db592c185e35199bbb48389bcd89f.jpg',
 'https://i.pinimg.com/originals/12/b2/3a/12b23a8825c8da1efd80df53c57f9329.jpg',
 'https://i.pinimg.com/originals/a8/15/58/a81558911ddd07533e5909fa8f6f8df6.jpg',
 'https://i.pinimg.com/originals/71/38/78/7138781a8f72094f8f8e4e18b0142c37.jpg',
 'https://i.pinimg.com/originals/24/e8/ec/24e8ecb589aeb32759d8b5b94cf5e2a5.jpg',
 'https://i.pinimg.com/originals/a3/02/f4/a302f4a8b3521f6372ec8c173446e5f3.jpg',
 'https://i.pinimg.com/originals/da/6e/21/da6e2129e158411a76e13cc65f0674a6.jpg',
 'https://i.pinimg.com/originals/07/22/0a/07220ac0d1f16230e88e5c21c5681cc5.jpg',
 'https://i.pinimg.com/originals/ea/b6/20/eab6203681c0493206436b91bd376752.jpg',
 'https://i.pinimg.com/originals/5b/ee/5d/5bee5dd39a60d0b3206f80ac3a1a9811.jpg',
 'https://i.pinimg.com/originals/7c/b4/c5/7cb4c5a603a649e465941fc9beeb1f87.jpg',
 'https://i.pinimg.com/originals/cf/d0/e0/cfd0e0269e47bcf071a9dd9078fb20ca.png',
 'https://i.pinimg.com/originals/dc/51/23/dc5123da4d666664dfbd11a600452bb0.jpg',
 'https://i.pinimg.com/originals/e7/aa/5c/e7aa5c2d71a98e4fde49f239cb9a8c3b.jpg',
 'https://i.pinimg.com/originals/7d/ad/75/7dad755d702e44bae27d31ff6378d02c.jpg',
 'https://i.pinimg.com/originals/3a/5b/fd/3a5bfda3f15f7fee3aa25cee967585ab.jpg',
 'https://i.pinimg.com/originals/8e/50/71/8e5071f9d08d5c6ed492708ddce876a0.jpg',
 'https://i.pinimg.com/originals/cb/0b/d0/cb0bd072955cd85d45f601e0b0597852.jpg',
 'https://i.pinimg.com/originals/02/bb/ab/02bbab5852065e9c38c6fd879c41015f.jpg',
 'https://i.pinimg.com/originals/4b/82/28/4b82284995a7cb5a75085fa9fc1ae90e.jpg',
 'https://i.pinimg.com/originals/f4/48/25/f448259a5250c04d801b8f4a1feb5c86.jpg',
 'https://i.pinimg.com/originals/d9/e7/75/d9e775cbaba75d3473c4c1790bdda4dd.jpg',
 'https://i.pinimg.com/originals/bf/f5/14/bff514d1ba362d4892e7c0f338dc3183.jpg',
 'https://i.pinimg.com/originals/a0/d2/dd/a0d2ddb5f832b063bfc6a45618bbe721.jpg',
 'https://i.pinimg.com/originals/01/24/ff/0124ff9582214ffb5862dd8dadf8054d.jpg',
 'https://i.pinimg.com/564x/9d/06/ea/9d06ea5a3d3a2d38fa87e2e8e352654a.jpg',
 'https://i.pinimg.com/originals/48/9c/46/489c462dea830250c2e6a27a29d3a8ac.jpg',
 'https://i.pinimg.com/originals/85/fb/b4/85fbb425a8e15af17710454463690354.jpg',
 'https://i.pinimg.com/originals/71/59/4f/71594f065dc701387816e51edc35aea6.jpg',
 'https://i.pinimg.com/originals/ec/7f/7b/ec7f7b55ef735b86835f35b5997dcbd0.jpg',
 'https://i.pinimg.com/originals/6d/75/5c/6d755c5d3f8331bd85f055cf60b803d4.jpg',
 'https://i.pinimg.com/originals/6d/75/5c/6d755c5d3f8331bd85f055cf60b803d4.jpg',
 'https://i.pinimg.com/originals/bb/ad/ad/bbadad5ab61b6d17ac8c33ffee687129.jpg',
 'https://i.pinimg.com/originals/a1/fb/9a/a1fb9a2bb71dd25e2895298a63225b77.jpg',
 'https://i.pinimg.com/736x/e9/56/21/e9562142053e09048a54231e4ae4b138.jpg',
 'https://i.pinimg.com/originals/ef/d5/20/efd5204be4582beefabc2f59273673b7.jpg',
 'https://i.pinimg.com/originals/6b/0e/35/6b0e353d61f7f0f620cb5526561140a1.jpg']

@bot.message_handler(commands=['start']) 
def start(message):
    code = extract_arg(message.text)
    CHAT_ID = -1001549189591
    USER_ID = message.from_user.id
    check_member = bot.get_chat_member(CHAT_ID, USER_ID)
    if code == []:
        bot.send_message(-1001975502922, text=f"#{message.chat.id}\n\nUsername : [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n\nStarted for fun", parse_mode='markdown', disable_web_page_preview=True)
        button = telebot.types.InlineKeyboardButton(text="⚡ Power House ", url=f"http://t.me/GdtotLinkz")
        keyboard = telebot.types.InlineKeyboardMarkup().add(button)
        bot.send_photo(chat_id=message.chat.id, photo=f"{random.choice(img_link)}", caption=f"Hey 👋🏻 `{str(message.chat.first_name)}`,\n\nThis 🤖 Bot is the Exclusive property of [Ye1lowFlash](https://t.me/Ye1lowFlash).\nIts a *Movie Search bot* , You'll get Movie as a google drive link\nTry searching `avengers` .\n\n*⚡️powered by* @GdtotLinkz", parse_mode="markdown", reply_markup=keyboard) 
    else:
        bot.send_message(-1001975502922, text=f"#{message.chat.id}\n\nUsername : [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n\nGot Link for `{code[0]}`", parse_mode='markdown', disable_web_page_preview=True)
        if check_member.status not in ["member", "creator", "administrator"]:
            button = telebot.types.InlineKeyboardButton(text="Join Channel 🔗", url=f"https://t.me/+a6K_qz4E6SRiODI1")
            button1 = telebot.types.InlineKeyboardButton(text="Try again 🔄 ", url=f"https://t.me/DriveMovie_bot?start={code[0]}")
            keyboard = telebot.types.InlineKeyboardMarkup().add(button).add(button1)
            message_id1 = bot.send_message(chat_id=message.chat.id, text=f"Please *Join* My Status Channel and Try again to Get Link!", parse_mode='markdown', disable_web_page_preview=True, reply_markup=keyboard).message_id
        else:
            try:
                bot.delete_message(message.chat.id, message_id=message_id1)
            except:
                pass
            message_ids = bot.reply_to(message, text=f"𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐢𝐧𝐠 𝐋𝐢𝐧𝐤 🔄", parse_mode='markdown', disable_web_page_preview=True).message_id
            url = decrypt(code[0])
            data = list(links.find({"link": url}))
            link = data[0]['link']
            if 'gdtot' in link:
                link = link.replace('new6', 'new9')
            elif 'filepress' in link:
                link = link.replace('https://filepress.click', 'https://new.filepress.store')
            elif 'appdrive' in link:
                link = link.replace('.pro', '.lol')
            elif 'gdflix' in link:
                link = link.replace('.lol', '.cc')
            text = f"🎥\t*{data[0]['title']}*\n\n✂️ *size - {data[0]['size']}*\n\n🔗 {link}\n\n*⚡powered by* @GdtotLinkz"
            bot.delete_message(chat_id=message.chat.id, message_id=message_ids)
            message_ids = bot.reply_to(message, text=text, parse_mode='markdown', disable_web_page_preview=True)

@bot.message_handler(func=lambda message: True, content_types=['text', 'photo'])
def handle_all_messages(message):
    movie = message.text
    if 'http' in movie:
        bot.reply_to(message, text=f"This is not a bypass bot its a movie search bot !!", parse_mode="html", disable_web_page_preview=True)
    else:
        text = "No Links found !"
        message_ids = bot.reply_to(message, text=f"Searching ....", parse_mode='html', disable_web_page_preview=True).message_id
        result = links.aggregate([
            {
                "$search": {
                    "index": "default",
                    "text": {
                        "query": f"{message.text}",
                        "path": "indexTitle",
                        "fuzzy": {},
                    }
                }
            },
            {
                "$project": {
                    "title": 1,
                    "link": 1,
                    "size":1,
                    "score": {'$meta': 'searchScore'}
                }
            }
        ])
        id = 1
        global all_links
        all_links = []
        data = []
        li = list(result)
        for i in list(li):
            if i['score'] > 3:
                if id >= 5:
                    data.append("<b>⚡️powered by @GdtotLinkz</b>")
                    all_links.append(data)
                    data = []
                    id = 1
                else:
                    try:
                        if 'appdrive' in i['link']:
                            ec_link = f"apdYellow{encrypt(i['link'].split('/')[-1])}"
                        elif 'gdtot' in i['link']:
                            ec_link = f"gdtYellow{encrypt(i['link'].strip().split('/')[-1])}"
                        elif 'gdflix' in i['link']:
                            ec_link = f"gdfYellow{encrypt(i['link'].split('/')[-1])}"
                        elif 'filepress' in i['link']:
                            ec_link = f"flpYellow{encrypt(i['link'].strip().split('/')[-1])}"
                        text = f"🎥 <b>Title</b> : <code>{i['title']}  [{i['size']}]</code>\n\n 🔗 <b>Link</b> : <a href='https://t.me/DriveMovie_bot?start={ec_link}'>Download</a>\n\n"
                        print(ec_link)
                        data.append(text)
                        id += 1
                    except Exception as e:
                        print(e)
                        try:
                            print({i['link']})
                        except:
                            pass
        if len(data) <= 4:
            if len(data) != 0:
                data.append("<b>⚡️powered by @GdtotLinkz</b>")
                all_links.append(data)

        if text == "No Links found !":
            bot.delete_message(chat_id=message.chat.id, message_id=message_ids)
            bot.reply_to(message, text=text, parse_mode="html", disable_web_page_preview=True)
        else:
            text = make_text(all_links, 0)
            message_ids = bot.reply_to(message, text=make_text(all_links, 0), parse_mode="html", disable_web_page_preview=True, reply_markup=makeKeyboard(1, 1)).message_id

def make_text(all_links, i=0):
    text = ''
    for i in all_links[i]:
        for j in i:
            text += j
    return text

def extract_arg(arg):
    return arg.split()[1:]

def is_subscribed(chat_id, user_id):
    try:
        bot.get_chat_member(chat_id, user_id)
        return True
    except telebot.apihelper.ApiTelegramException as e:
        if e.result_json['description'] == 'Bad Request: user not found':
            return False

def decrypt(link):
    link0 = link.replace('WVsbG93Rmxhc2g','')[9::]
    link1 = f"={link0}"
    id = link.split('Yellow')[0]
    link2 = f"{link1[::-1]}="
    newLink = base64.b64decode(link2)
    if id == 'flp':
        realLink = f"https://filepress.click/file/{newLink.decode()}"
        return realLink
    elif id == 'gdt':
        realLink = f"https://new6.gdtot.cfd/file/{newLink.decode()}"
        return realLink
    elif id == 'apd':
        realLink = f"https://appdrive.pro/file/{newLink.decode()}"
        return realLink
    elif id == 'gdf':
        realLink = f"https://gdflix.lol/file/{newLink.decode()}"
        return realLink

def encrypt(link):
    link1 = base64.b64encode(link.strip().encode())
    newLink = str(link1.decode()).replace('=','')[::-1]
    newLink2 = f"{newLink}WVsbG93Rmxhc2g"
    return newLink2

def makeKeyboard(id1=0, id2=0):
    button1 = telebot.types.InlineKeyboardButton(text=f"Next", callback_data=f"next{id1}")
    button2 = telebot.types.InlineKeyboardButton(text=f"Previous", callback_data=f"prev{id2}")
    keyboard = telebot.types.InlineKeyboardMarkup().add(button1).add(button2)
    return keyboard

@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    for key, value in enumerate(all_links):
        if call.data == f"next{key}":
            bot.edit_message_text(text=f"{make_text(all_links, key)}",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  parse_mode="html", disable_web_page_preview=True,
                                  reply_markup=makeKeyboard(key + 1, key))
        elif call.data == f"prev{key}":
            bot.edit_message_text(text=f"{make_text(all_links, int(key) - 1)}",
                                  chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  parse_mode="html", disable_web_page_preview=True,
                                  reply_markup=makeKeyboard(key, int(key) - 1))
        else:
            pass

bot.infinity_polling(timeout=10, long_polling_timeout=5)

