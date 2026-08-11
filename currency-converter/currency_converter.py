"""CLI currency converter using fixed reference rates.

The rates are intentionally stored locally so the program works without an API
key or internet connection. They are sample rates for learning purposes and
should not be used for financial decisions.
"""

from decimal import Decimal, InvalidOperation

# Approximate units per 1 USD. Update these values when using current rates.
RATES_TO_USD = {
    "USD": Decimal("1.00"),
    "EUR": Decimal("1.09"),
    "GBP": Decimal("1.27"),
    "SEK": Decimal("0.096"),
    "NOK": Decimal("0.094"),
    "DKK": Decimal("0.146"),
    "CHF": Decimal("1.13"),
    "CAD": Decimal("0.73"),
    "AUD": Decimal("0.65"),
    "NZD": Decimal("0.60"),
    "JPY": Decimal("0.0067"),
    "CNY": Decimal("0.138"),
    "INR": Decimal("0.012"),
    "PKR": Decimal("0.0036"),
    "BDT": Decimal("0.0084"),
    "AED": Decimal("0.2723"),
    "SAR": Decimal("0.2667"),
    "TRY": Decimal("0.0305"),
    "PLN": Decimal("0.255"),
    "CZK": Decimal("0.0435"),
    "HUF": Decimal("0.00275"),
    "BRL": Decimal("0.184"),
    "MXN": Decimal("0.054"),
    "ZAR": Decimal("0.054"),
    "KRW": Decimal("0.00075"),
    "SGD": Decimal("0.74"),
    "HKD": Decimal("0.128"),
    "THB": Decimal("0.028"),
    "MYR": Decimal("0.235"),
}

CURRENCY_NAMES = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "SEK": "Swedish Krona",
    "NOK": "Norwegian Krone",
    "DKK": "Danish Krone",
    "CHF": "Swiss Franc",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "NZD": "New Zealand Dollar",
    "JPY": "Japanese Yen",
    "CNY": "Chinese Yuan",
    "INR": "Indian Rupee",
    "PKR": "Pakistani Rupee",
    "BDT": "Bangladeshi Taka",
    "AED": "UAE Dirham",
    "SAR": "Saudi Riyal",
    "TRY": "Turkish Lira",
    "PLN": "Polish Zloty",
    "CZK": "Czech Koruna",
    "HUF": "Hungarian Forint",
    "BRL": "Brazilian Real",
    "MXN": "Mexican Peso",
    "ZAR": "South African Rand",
    "KRW": "South Korean Won",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "THB": "Thai Baht",
    "MYR": "Malaysian Ringgit",
}


def display_currencies():
    print("\nAvailable currencies:\n")
    for code, name in CURRENCY_NAMES.items():
        print(f"  {code:<4} - {name}")


def get_currency(prompt):
    while True:
        code = input(prompt).strip().upper()
        if code in RATES_TO_USD:
            return code
        print("Invalid currency code. Type LIST to see available currencies.")


def get_amount():
    while True:
        value = input("Enter amount: ").strip()
        try:
            amount = Decimal(value)
            if amount < 0:
                raise ValueError
            return amount
        except (InvalidOperation, ValueError):
            print("Please enter a valid non-negative number.")


def convert(amount, from_currency, to_currency):
    # Convert source -> USD -> target.
    amount_in_usd = amount * RATES_TO_USD[from_currency]
    return amount_in_usd / RATES_TO_USD[to_currency]


def show_rate(from_currency, to_currency):
    rate = convert(Decimal("1"), from_currency, to_currency)
    print(f"1 {from_currency} = {rate:.6f} {to_currency}")


def main():
    print("=" * 50)
    print("        CLI CURRENCY CONVERTER")
    print("=" * 50)
    print(f"Currencies supported: {len(RATES_TO_USD)}")
    print("Type LIST to see currencies or Q to quit.\n")

    while True:
        from_currency = input("From currency: ").strip().upper()
        if from_currency == "Q":
            print("Goodbye!")
            break
        if from_currency == "LIST":
            display_currencies()
            continue
        if from_currency not in RATES_TO_USD:
            print("Invalid currency code. Type LIST to see available currencies.\n")
            continue

        to_currency = get_currency("To currency: ")
        amount = get_amount()
        result = convert(amount, from_currency, to_currency)

        print("\n" + "-" * 50)
        print(f"{amount:,.2f} {from_currency} = {result:,.2f} {to_currency}")
        show_rate(from_currency, to_currency)
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
