import urllib.request

import telebot

token = '963907902:AAGlt2q0bFd2gxhYjp4rnKlNILzP8PefpxM'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    start_text = "Бот позволит тебе быть в курсе изменения валют."
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(commands=['btc', 'us-btc'])
def handle_start_help(message):
    start_text = "За один BTC сейчас предлагают {} долларов.".format(us_btc())
    bot.send_message(message.chat.id, start_text)


########################
### Common #############
########################
def us_btc():
	response = urllib.request.urlopen('https://blockchain.info/q/24hrprice')
	online_course = response.read().decode()
	saved_course = read_btc_file()
	if float(online_course) is not float(saved_course):
		save_btc_course(online_course)

	result = online_course
	print(result)
	return result

def save_btc_course(btc_cur):
	with open('btc.db', 'w') as f: 
		f.write(str(btc_cur)) 

def read_btc_file():
	with open('btc.db') as f: 
		data = f.readlines()
	try:
		return data[0]
	except Exception as e:
		return 0


if __name__ == '__main__':
    print("Currency_bot Started")
    bot.polling(none_stop=True)
