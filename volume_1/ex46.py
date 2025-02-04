import random

def get_exchange_rate(from_currency, to_currency):
    rates = {
        ("USD", "EUR"): 0.92, ("USD", "GBP"): 0.78, ("USD", "JPY"): 145.32, ("USD", "CNY"): 7.1,
        ("EUR", "USD"): 1.09, ("EUR", "GBP"): 0.85, ("EUR", "JPY"): 158.22, ("EUR", "CNY"): 7.7,
        ("GBP", "USD"): 1.28, ("GBP", "EUR"): 1.18, ("GBP", "JPY"): 185.45, ("GBP", "CNY"): 9.02,
        ("JPY", "USD"): 0.0069, ("JPY", "EUR"): 0.0063, ("JPY", "GBP"): 0.0054, ("JPY", "CNY"): 0.048,
        ("CNY", "USD"): 0.14, ("CNY", "EUR"): 0.13, ("CNY", "GBP"): 0.11, ("CNY", "JPY"): 20.83,
        ("CNY", "CNY"): 1.0, ("USD", "USD"): 1.0, ("EUR", "EUR"): 1.0, ("GBP", "GBP"): 1.0, ("JPY", "JPY"): 1.0
    }
    return rates.get((from_currency, to_currency), random.uniform(0.5, 1.5))

def main():
    currencies = ["USD", "EUR", "GBP", "JPY", "CNY"]
    from_currency = input(f"Enter the currency to convert from {currencies}: ").upper()
    if from_currency not in currencies:
        print("Invalid currency.")
        return
    to_currency = input(f"Enter the currency to convert to {currencies}: ").upper()
    if to_currency not in currencies or to_currency == from_currency:
        print("Invalid conversion.")
        return
    try:
        amount = float(input("Enter the amount: "))
        if amount < 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return
    rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * rate
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency} at a rate of {rate:.4f}.")

if __name__ == "__main__":
    main()