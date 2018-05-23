# -*-coding:utf-8 -*-
from util_service import download_sample, reply_msg
from app_message.message import *
from machine_service import read_file, analyze_transation, get_final_result


def receive_txt(bot, update):
    """
    :param bot:
    :param update:
    :return:
    """
    try:
        message = get_message(update)
        user_name, chat_id = get_username(update)
        content = str(message.text)
        print user_name, chat_id
        print content
        possible = analyze_transation(content)
        if not possible:
            reply_msg(bot, chat_id, M4)
            return
        txt = M2 % possible
        reply_msg(bot, chat_id, txt)

        txt = get_final_result(possible, M3)
        reply_msg(bot, chat_id, txt)

    except Exception, e:
        print "receive_txt", e


def receive_document(bot, update):
    try:
        message = get_message(update)
        user_name, chat_id = get_username(update)
        document = message.document
        file_id = str(document.file_id)
        file_url = str(bot.getFile(file_id).file_path)
        file_name = str(document.file_name)
        file_type = str(document.mime_type)
        if "sample" in file_name:
            if "csv" in file_type:
                file_path = download_sample(file_url, file_name)
                if file_path:
                    reply_msg(bot, chat_id, M1)
                    read_file(file_path, bot, chat_id)
    except Exception, e:
        print("receive_document", e)


def get_message(update):
    if update.edited_message:
        message = update.edited_message
    else:
        message = update.message
    return message


def get_username(update):
    message = get_message(update)

    chat = message.chat
    chat_id = int(chat.id)
    # 来自群
    if chat_id < 0:
        user = message.from_user
        username = '(@' + str(user.username) + '|' + str(user.first_name) + '|' + str(user.last_name) + ')'
    # 来自用户
    else:
        chat = message.chat
        username = '(@' + str(chat.username) + '|' + str(chat.first_name) + '|' + str(chat.last_name) + ')'
    return username, chat_id







