"""
Initializing Telegram bot instance with aiogram
"""
import telebot

from settings import config
from settings.logger import log


bot = telebot.TeleBot(token=config.TELEGRAM_BOT_TOKEN)
log.info('Bot has been initialized')
