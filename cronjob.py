import urllib.request
from math import fabs

from currency_bot import save_btc_course, read_btc_file, bot

differ = 10

def us_btc():
        response = urllib.request.urlopen('https://blockchain.info/q/24hrprice')
        online_course = float(response.read().decode())
        saved_course = float(read_btc_file())
        if online_course is not saved_course:
                if fabs(saved_course - online_course) > differ:
                        bot.send_message(611317205, 'Курс BTC заметно изменился и теперь составляет ${}'.format(online_course))
                save_btc_course(online_course)

        result = online_course
        #print(result)
        return result

us_btc()

