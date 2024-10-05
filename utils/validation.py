def validate_currency_code(currency_code: str) -> bool:
    """Validate if the given currency code is in the correct format."""
    return len(currency_code) == 3 and currency_code.isalpha()