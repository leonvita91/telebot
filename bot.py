import os 
import telebot
teletok = os.environ.get('tokentele')

bot = telebot.TeleBot(teletok)
#massage handler
text = 'My bot is alive :)'
@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message, text)

@bot.message_handler(func=lambda msg : True)
def recive(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()
