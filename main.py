from binance.client import Client

client = Client()
print(client.get_historical_klines('BTCUSDT', '1d', '2025-02-15'))
