import telebot
import ast
import time
from telebot import types

bot = telebot.TeleBot("731167915:AAGWcrd09zSlEwpphUANLHctvDQSDd_ImN8")

stringList = {"Name": "английский", "Language": "шотландский"}
stringList1 = {"Name": "мэнский"}
crossIcon = u"\u274C"

def makeKeyboard():   
    markup = types.InlineKeyboardMarkup()
    
    for key, value in stringList.items():
        markup.add(types.InlineKeyboardButton(text=value,
                                              callback_data="['value', '" + value + "', '" + key + "']"))
    for key, value in stringList1.items():    
        markup.add(types.InlineKeyboardButton(text=value,
                                   callback_data="['value', '" + value + "', '" + key + "']"))

    return markup

@bot.message_handler(commands=['test'])
def handle_command_adminwindow(message):
    
    bot.send_message(chat_id=message.chat.id,
                     text="На каком языке говорят на острове Мэн?",
                     reply_markup=makeKeyboard(),
                     parse_mode='HTML')

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    if (call.data.startswith("['value'")):
        valueFromCallBack = ast.literal_eval(call.data)[1]
        bot.answer_callback_query(callback_query_id=call.id,
                              show_alert=True,
                              text="Вы ответили " + valueFromCallBack + " правильный ответ ирландский")


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)
