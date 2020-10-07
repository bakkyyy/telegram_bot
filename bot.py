import telebot
bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def message(m):
	chat = "437126316"
	text = "Имя пользователя: " + str(m.chat.username) + '\n' + "Имя Фамилия: " + str(m.chat.first_name) + " " + str(m.chat.last_name) + '\n' + "Текст: " + str(m.text)
	bot.send_message(chat, text)
bot.polling(none_stop=True, interval=0)
