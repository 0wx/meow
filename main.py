from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('http://aws.random.cat/meow').json()    
    url = contents['file']
    return url

def meow(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('bot_token')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('meow',meow))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
