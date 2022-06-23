# -*- coding: utf-8 -*-
import schedule
import logging
from datetime import datetime
import pandas
from setting import *
from time import sleep
from threading import Thread

excel_plan = pandas.read_excel(path, sheet_name='Moscow')
number_of_rows = len(excel_plan)
list_plan_canal = []
for i in range(number_of_rows):
    row = list(excel_plan.iloc[i])
    list_plan_canal.append(row)


logger = telebot.logger
logger.setLevel(logging.DEBUG)


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


def send_message(list_into):
    data_now = datetime.now()
    data_now_format = data_now.strftime("%d-%m-%Y")
    time_format = data_now.strftime("%H:%M:%S")
    for j in range(len(list_into)):
        data_list_plan_canal = str(list_into[j][0])
        if data_now_format == data_list_plan_canal:
            time_1 = time1
            time_2 = time2
            time_3 = time3
            time_list = str(list_into[j][1])
            if time_1 == time_list == time_format:
                text = list_into[j][3]
                photo = list_into[j][2]
                with open(photo, 'rb') as f:
                    bot.send_photo(CHANNEL_NAME, f, caption=text)
                break
            elif time_2 == time_list == time_format:
                text = list_into[j][3]
                photo = list_into[j][2]
                with open(photo, 'rb') as f:
                    bot.send_photo(CHANNEL_NAME, f, caption=text)
                break
            elif time_3 == time_list == time_format:
                text = list_into[j][3]
                photo = list_into[j][2]
                with open(photo, 'rb') as f:
                    bot.send_photo(CHANNEL_NAME, f, caption=text)
                break


schedule.every().day.at(time1).do(send_message, list_plan_canal)
schedule.every().day.at(time2).do(send_message, list_plan_canal)
schedule.every().day.at(time3).do(send_message, list_plan_canal)

Thread(target=schedule_checker).start()

