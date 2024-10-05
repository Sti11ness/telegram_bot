from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()

    if query.data == 'get_rate':
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
        await query.edit_message_text(text="Please choose a currency:", reply_markup=reply_markup)

    elif query.data.startswith('rate_'):
        currency_code = query.data.split('_')[1]
        from services.currency_service import get_exchange_rate

        try:
            rate = get_exchange_rate(currency_code)
            await query.edit_message_text(text=f"The current exchange rate for {currency_code} to RUB is: {rate}")
        except ValueError as e:
            await query.edit_message_text(text=str(e))