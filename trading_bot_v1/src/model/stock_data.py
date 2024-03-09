class StockData:
    def __init__(self, timestamp, open, close, volume,
                 rsi):
        self.timestamp = timestamp
        self.close = close
        self.open = open
        self.volume = volume
        self.rsi = rsi
