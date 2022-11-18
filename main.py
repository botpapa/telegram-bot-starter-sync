"""
Launch this file to start the bot
"""
from telebot.types import Message
from settings.bot import bot


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
def message_handler(message: Message):
    bot.reply_to(message, 'It\'s working')


# Starting bot polling
bot.polling()
