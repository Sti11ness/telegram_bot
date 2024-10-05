import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPEN_EXCHANGE_RATES_API_KEY")
BASE_URL = "https://openexchangerates.org/api/latest.json"

def get_exchange_rate(currency_code: str) -> float:
    """Get the exchange rate for the given currency to RUB."""
    response = requests.get(f"{BASE_URL}?app_id={API_KEY}&symbols={currency_code},RUB")
    if response.status_code != 200:
        raise ValueError("Failed to fetch exchange rates. Please try again later.")

    data = response.json()
    if currency_code not in data["rates"] or "RUB" not in data["rates"]:
        raise ValueError(f"Currency code '{currency_code}' is not supported.")

    rate_to_rub = data["rates"]["RUB"] / data["rates"][currency_code]
    return round(rate_to_rub, 2)