# -*- coding: UTF-8 -*-
# __author__ = 'Sengo'
from util_service import reply_msg
import pandas as pd
from app_base.utils import get_int
from math import log


def read_file(file_path, bot, chat_id):
    try:
        data = pd.read_csv(file_path)
        read_data = str(data.head())
        reply_msg(bot, chat_id, read_data)

        reply_msg(bot, chat_id, str(data.fraudulent.value_counts()))
        reply_msg(bot, chat_id, str(data.card_country.value_counts()))

    except Exception, e:
        print "machine_learning", e


def analyze_transation(transation):
    s = split_data(transation)
    if not s:
        return
    amount = s.get("amount")
    print get_int(amount)
    card_use_24h = s.get("use")
    country = s.get("country")
    cc_au = 0
    cc_gb = 0
    if country == "AU":
        cc_au = 1
    if country == "GB":
        cc_gb = 1
    x = (4.63*10**-6)*get_int(amount) + 0.035*get_int(card_use_24h) \
        + 0.0043*get_int(cc_au) + 0.0025*get_int(cc_gb) - 0.016
    a = 2**x
    return a/(1+a)


def split_data(s):
    try:
        data = s.split(",")
        re = {}
        for d in data:
            d = d.split("=")
            if len(d) != 2:
                return
            prefix = d[0]
            num = d[1]
            if "AMOUNT" in prefix:
                re['amount'] = d[1]
            if "COUNTRY" in prefix:
                re['country'] = d[1]
            if "USE" in prefix:
                re["use"] = d[1]
        if len(re) == 3:
            return re
        return False
    except Exception, e:
        print "split_data", e


def get_final_result(possible, M3):
    if possible > 0.5:
        txt = M3 % (possible, "larger", "is not")
    else:
        txt = M3 % (possible, "smaller", "is")
    return txt


if __name__ == '__main__':
    t = "AMOUNT-2000,COUNTRY-US,USE-3"
    print analyze_transation(t)

