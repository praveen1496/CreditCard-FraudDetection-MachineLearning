# -*- coding: utf-8 -*-
import sys
from telegram.ext import Updater, MessageHandler, Filters
import logging
from app_service.telegram_service import receive_txt, receive_document
from settings import BOT_TOKEN
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(token=BOT_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, receive_txt, allow_edited=False))
    dp.add_handler(MessageHandler(Filters.document, receive_document, allow_edited=True))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()
