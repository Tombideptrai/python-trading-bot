from binance import ThreadedWebsocketManager
from database import Database

class WebSocket:

    def __init__(self, symbol = "BTCUSDT", interval = "1m"):
        
        self.symbol = symbol
        self.interval = interval
        self.db = Database()
        self.wsm = ThreadedWebsocketManager()

    def handle_message(self, msg):

        if msg['e'] == "kline":

            kline = msg['k']

            if kline['x']:

                timestamp = kline['t']
                open_price = float(kline['o'])
                high_price = float(kline['h'])
                low_price = float(kline['l'])
                close_price = float(kline['c'])
                volume = float(kline('v'))

        self.db.insert_data(self.symbol.upper(), timestamp, open_price, high_price, low_price, close_price, volume)

    def start(self):
        
        print(f"Starting Websocket for {self.symbol}")
        self.twm.start()
        self.twm.start_kline_socket(callback = self.handle_message, symbol=self.symbol, interval = self.interval)

    def stop(self):

        print(f"Stopping Websocket...")
        self.twm.stop()
        print(f"Websocket stopped.")