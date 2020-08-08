from telegram.exe import Update, CommandHandler
from tim import strftime
up = from telegram.ext import Updater, CommandHandler
from time import strftime

up = Updater('542859904:AAGi19EvA5FBxrpVpD5CGNh9bkNLUcyDLmM')


def Horas(bot, update):

    msg = "Olá {user_name} agora são: "
    msg += strftime('%H:%M:%S')

    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name))


up.dispatcher.add_handler(CommandHandler('horas', Horas))
up.start_polling()