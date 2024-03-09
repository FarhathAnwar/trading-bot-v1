from trading_bot_v1.src.service.data_service import parse_csv, filter_stock_data


def main():
    filename = '../resources/dummyData.csv'
    stock_data_list = parse_csv(filename)
    filtered_data = filter_stock_data(stock_data_list)

    # Output the filtered data
    for stock_data in filtered_data:
        print(
            f"Date: {stock_data.timestamp}, open: {stock_data.open}, close: {stock_data.close}, RSI: {stock_data.rsi}")


if __name__ == "__main__":
    main()
