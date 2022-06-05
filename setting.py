# -*- coding: utf-8 -*-
import os

import telebot


bot = telebot.TeleBot('BOT_TOKEN')

CHANNEL_NAME = os.environ.get('CHANNEL_NAME')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

path = r'/app/files/Plan.xlsx'

time1 = "06:00:00"
time2 = "09:00:00"
time3 = "15:00:00"
