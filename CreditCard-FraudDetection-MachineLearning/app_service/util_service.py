# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from settings import SAMPLE_PATH
import urllib
import os


def download_sample(url, file_name):
    try:
        file_path = os.path.join(SAMPLE_PATH, file_name)
        urllib.urlretrieve(url, file_path)
        print "download %s success" % file_name
        return file_path
    except Exception, e:
        print "download_sample", e


def reply_msg(bot, chat_id, txt):
    try:
        bot.send_message(chat_id=chat_id, text=txt)
        return True
    except Exception, e:
        print "reply_msg", e