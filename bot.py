import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
import os
from config.settings import TELEGRAM_TOKEN
from handlers.start_handler import start
from handlers.stop_handler import stop
from handlers.callback_handler import button_callback
from handlers.rate_handler import rate
from handlers.unknown_handler import unknown_command
from handlers.error_handler import error_handler

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("rate", rate))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.Command, unknown_command))

    # Error handler
    application.add_error_handler(error_handler)

    # Start the bot
    application.run_polling()