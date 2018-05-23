# -*-coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG_PROJECT = True

BOT_TOKEN = '452687804:AAFNUhJ2zvAwC8-8WT-xdYaDfVV7EI244yc'

SOCKET_TIME_OUT = 30

SAMPLE_PATH = BASE_DIR + "/sample/"

DB_KWARGS = dict(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='543%$#',
    db='db_bot',
    charset="utf8"
)

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,
    'password': None,
    'expire': 7*24*60*60,
}
