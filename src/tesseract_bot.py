#! /usr/bin/env python3

import logging
import handler
import argparse
import config
import errno
import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

def resolve_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--verbose', action='store_true')
	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.DEBUG,
							format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
	resolve_args()

	os.chdir(os.path.split(os.path.abspath(__file__))[0])

	try:
	    os.mkdir(config.CACHE_DIR)
	except OSError as e:
	    if e.errno != errno.EEXIST:
	        raise e

	updater = Updater(token=config.BOT_TOKEN)

	dispatcher = updater.dispatcher

	print(updater.bot.getMe())

	start_handler = CommandHandler('start', handler.start)
	dispatcher.add_handler(start_handler)

	help_handler = CommandHandler('help', handler.help)
	dispatcher.add_handler(help_handler)

	lang_handler = CommandHandler('lang',handler.lang)
	dispatcher.add_handler(lang_handler)

	tesseract_handler = CommandHandler('tesseract',handler.tesseract)
	dispatcher.add_handler(tesseract_handler)

	total_handler = CommandHandler('total',handler.totalvalues)
	dispatcher.add_handler(total_handler)

	delete_handler = CommandHandler('delete',handler.delete_last)
	dispatcher.add_handler(delete_handler)

	manual_handler = CommandHandler('manual',handler.update_manually)
	dispatcher.add_handler(manual_handler)

	message_handler = MessageHandler(Filters.photo,handler.messages)
	dispatcher.add_handler(message_handler)

	unknown_handler = MessageHandler(Filters.command,handler.unknown)
	dispatcher.add_handler(unknown_handler)


	updater.start_polling()

if __name__ == '__main__':
	main()