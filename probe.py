import schedule
from datetime import datetime
from threading import Thread
import pandas
import telebot
from time import sleep
import logging

logger = telebot.logger
logger.setLevel(logging.DEBUG)

time1 = "20:16:00"
path = r'files/Plan.xlsx'

BOT_TOKEN_1 = '5458380415:AAFkGKr3e9eysde1jbh0aQJJh7YuP5PvvRM'
bot_1 = telebot.TeleBot(BOT_TOKEN_1)
CHANNEL_NAME = '@test_avv'


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def function_to_run(list_into):
    data_now = datetime.now()
    data_now_format = data_now.strftime("%d-%m-%Y")
    time_format = data_now.strftime("%H:%M:%S")
    for j in range(len(list_into)):
        data_list_plan_canal = str(list_into[j][0])
        if data_now_format == data_list_plan_canal:
            time_1 = time1
            time_list = str(list_into[j][1])
            if time_1 == time_list == time_format:
                text = list_into[j][3]
                photo = list_into[j][2]
                text_photo = [text, photo]
                with open(photo, 'rb') as f:
                    bot_1.send_photo(CHANNEL_NAME, f, caption=text)
                break


excel_plan = pandas.read_excel(path, sheet_name='Moscow')
number_of_rows = len(excel_plan)
list_plan_canal = []
for i in range(number_of_rows):
    row = list(excel_plan.iloc[i])
    list_plan_canal.append(row)

Thread(target=schedule_checker).start()
schedule.every().day.at(time1).do(function_to_run, list_plan_canal)
# schedule.every().day.at(time2).do(function_to_run, list_plan_canal)
# schedule.every().day.at(time3).do(function_to_run, list_plan_canal)
try:
    bot_1.polling(none_stop=True)
except:
    pass
