from telegram import Update
from telegram.ext import ContextTypes

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /stop command to stop interactions."""
    await update.message.reply_text("Thank you for using our bot. The interaction has been stopped. You can start again with /start.")
