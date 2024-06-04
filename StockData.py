def calculate_average_closing_price(stock_data, stock_symbol, start_date, end_date):
    total_closing_price = 0
    count = 0

    for entry in stock_data:
        symbol, date, closing_price = entry
        if symbol == stock_symbol and start_date <= date <= end_date:
            total_closing_price += closing_price
            count += 1

    if count == 0:
        return None  # No data found for the specified stock and date range
    else:
        return total_closing_price / count

def main():
    # Sample data
    stock_data = [
		("AAPL", "2021-01-01", 130.0),
		("AAPL", "2021-01-02", 132.0),
		("AAPL", "2021-01-03", 134.0),
		("AMZN", "2021-01-01", 3200.0),
		("AMZN", "2021-01-02", 3250.0),
		("AMZN", "2021-01-03", 3300.0),
		("GOOGL", "2021-01-01", 1800.0),
		("GOOGL", "2021-01-02", 1825.0),
		("GOOGL", "2021-01-03", 1850.0),
		("MSFT", "2021-01-01", 220.0),
		("MSFT", "2021-01-02", 225.0),
		("MSFT", "2021-01-03", 250.0),
    ]

    while True:
        print("\n1. Calculate average closing price for a stock over a given period")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stock_symbol = input("Enter the stock symbol: ")
            start_date = input("Enter the start date (YYYY-MM-DD): ")
            end_date = input("Enter the end date (YYYY-MM-DD): ")

            average_price = calculate_average_closing_price(stock_data, stock_symbol, start_date, end_date)
            if average_price is not None:
                print(f"The average closing price of {stock_symbol} from {start_date} to {end_date} is: {average_price}")
            else:
                print("No data found for the specified stock and date range.")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
