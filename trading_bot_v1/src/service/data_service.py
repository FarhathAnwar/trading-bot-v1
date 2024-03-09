import pandas as pd
from ..model.stock_data import StockData


def parse_csv(filename):
    df = pd.read_csv(filename)
    stock_data_list = []
    for index, row in df.iterrows():
        stock_data = StockData(
            row['Timestamp'], row['Open'], row['Close'], row['Volume'],
            row['RSI']
        )
        stock_data_list.append(stock_data)
    return stock_data_list


def filter_stock_data(stock_data_list):
    filtered_data = []
    for stock_data in stock_data_list:
        # print(stock_data.rsi14)
        if isinstance(stock_data.rsi, (int, float)) and stock_data.rsi < 40:
            filtered_data.append(stock_data)
    return filtered_data
