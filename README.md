# Currency Exchange Telegram Bot

This is a modular Telegram bot that provides exchange rates for different currencies in relation to the Russian Ruble (RUB). It uses the Open Exchange Rates API to fetch current exchange rates.

## Features
- `/start` - Sends a welcome message and instructions on how to use the bot. Includes interactive menus for easy navigation.
- `/rate [currency_code]` - Provides the exchange rate of the specified currency to RUB (e.g., `/rate USD`).
- Interactive button-based interface for selecting currencies.
- Permanent menu with frequently used options for navigating commands.

## Setup
1. Clone the repository.
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the `currency_bot` directory and add your credentials:
   ```
   TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
   OPEN_EXCHANGE_RATES_API_KEY=YOUR_API_TOKEN
   ```
5. Run the bot:
   ```
   python bot.py
   ```

## Usage
- Start the bot in Telegram and use the `/start` command to get instructions.
- Use `/rate [currency_code]` to get the current exchange rate for that currency to RUB.
- Alternatively, use the button-based interface to get exchange rates or navigate the bot's functions.