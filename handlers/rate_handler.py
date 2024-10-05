import time
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from services.currency_service import get_exchange_rate
from utils.validation import validate_currency_code

# Dictionary to track user requests and prevent spamming
user_requests = {}

async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /rate command to provide the exchange rate of the given currency."""
    user_id = update.effective_user.id
    current_time = time.time()

    # Check request frequency to prevent spamming
    if user_id in user_requests and current_time - user_requests[user_id] < 5:
        await update.message.reply_text("Please wait a few seconds before making another request.")
        return

    # Update the time of the last request
    user_requests[user_id] = current_time

    # Display the list of available currencies as buttons
    currency_buttons = [
        [InlineKeyboardButton("USD", callback_data='rate_USD')],
        [InlineKeyboardButton("EUR", callback_data='rate_EUR')],
        [InlineKeyboardButton("JPY", callback_data='rate_JPY')],
        [InlineKeyboardButton("GBP", callback_data='rate_GBP')],
        [InlineKeyboardButton("AUD", callback_data='rate_AUD')],
        [InlineKeyboardButton("CAD", callback_data='rate_CAD')],
        [InlineKeyboardButton("CHF", callback_data='rate_CHF')],
        [InlineKeyboardButton("CNY", callback_data='rate_CNY')],
        [InlineKeyboardButton("HKD", callback_data='rate_HKD')],
        [InlineKeyboardButton("NZD", callback_data='rate_NZD')],
        [InlineKeyboardButton("SEK", callback_data='rate_SEK')],
        [InlineKeyboardButton("KRW", callback_data='rate_KRW')],
        [InlineKeyboardButton("SGD", callback_data='rate_SGD')],
        [InlineKeyboardButton("NOK", callback_data='rate_NOK')],
        [InlineKeyboardButton("MXN", callback_data='rate_MXN')],
        [InlineKeyboardButton("INR", callback_data='rate_INR')],
        [InlineKeyboardButton("ZAR", callback_data='rate_ZAR')],
        [InlineKeyboardButton("TRY", callback_data='rate_TRY')],
        [InlineKeyboardButton("BRL", callback_data='rate_BRL')],
    ]
    reply_markup = InlineKeyboardMarkup(currency_buttons)
    await update.message.reply_text("Please choose a currency:", reply_markup=reply_markup)