# 💱 CLI Currency Converter

A simple command-line currency converter built with Python. It supports **29 currencies** and converts between any two supported currencies.

## ✨ Features

- 💱 29 supported currencies
- 🖥️ Command-line interface
- 🔢 Decimal-based calculations for better numeric precision
- ✅ Input validation
- 📋 `LIST` command to display all supported currencies
- 🔁 Convert between any supported currency pair
- 📈 Display the calculated exchange rate
- 🌐 Works offline because rates are stored locally
- 🚫 No API key required

## 💰 Supported Currencies

USD, EUR, GBP, SEK, NOK, DKK, CHF, CAD, AUD, NZD, JPY, CNY, INR, PKR, BDT, AED, SAR, TRY, PLN, CZK, HUF, BRL, MXN, ZAR, KRW, SGD, HKD, THB, MYR.

## ▶️ How to Run

From this directory, run:

```bash
python currency_converter.py
```

Then enter the source currency, target currency, and amount.

Example:

```text
From currency: USD
To currency: EUR
Enter amount: 100

100.00 USD = 91.74 EUR
1 USD = 0.917431 EUR
```

## 📋 List Currencies

Type `LIST` when asked for the source currency to display every supported currency and its name.

## 🧠 Concepts Practiced

- Dictionaries
- Functions
- Loops
- Conditional statements
- Input validation
- String formatting
- `decimal.Decimal`
- Data organization
- Currency conversion logic

## ⚠️ About Exchange Rates

The project uses **approximate, locally stored sample rates** so it can run without an internet connection. Exchange rates change constantly, so these values should not be used for real financial decisions.

A future version could connect to a live exchange-rate API and update the rates automatically.
