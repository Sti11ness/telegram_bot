from telegram import Update
from telegram.ext import ContextTypes

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle unknown commands."""
    await update.message.reply_text("Sorry, I didn't understand that command. Please use /start for a list of available commands.")