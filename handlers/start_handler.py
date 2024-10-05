from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued with buttons."""
    user = update.effective_user

    # Создание кнопок inline-меню для первой команды
    inline_keyboard = [
        [InlineKeyboardButton("Получить курс валюты", callback_data='get_rate')],
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    await update.message.reply_html(
        rf"Hello, {user.mention_html()}! Welcome to the Currency Exchange Bot.\n"
        "Use the button below to get started.",
        reply_markup=reply_markup
    )