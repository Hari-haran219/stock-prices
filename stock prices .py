stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

portfolio = {}

print("Enter your stock holdings. Type 'done' to finish.")
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            raise ValueError
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid positive integer for quantity.")

total_value = 0
print("\n--- Portfolio Summary ---")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    print(f"{stock}: {quantity} shares @ ${price} = ${value}")
    total_value += value

print(f"\nTotal Investment: ${total_value}")

save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    file_type = input("Enter file type (txt/csv): ").lower()
    if file_type == "txt":
        with open("portfolio_summary.txt", "w") as file:
            for stock, quantity in portfolio.items():
                file.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * quantity}\n")
            file.write(f"\nTotal Investment: ${total_value}")
        print("Saved to portfolio_summary.txt")
    elif file_type == "csv":
        with open("portfolio_summary.csv", "w") as file:
            file.write("Stock,Quantity,Price,Total\n")
            for stock, quantity in portfolio.items():
                file.write(f"{stock},{quantity},{stock_prices[stock]},{stock_prices[stock] * quantity}\n")
            file.write(f",,,{total_value}")
        print("Saved to portfolio_summary.csv")
    else:
        print("Invalid file type. Nothing saved.")
