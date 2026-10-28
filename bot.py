import time
import yfinance as yf

class IndianMarketBot:
    def __init__(self):
        self.market_name = "Indian Stock Market (NSE)"
        self.symbol = "^NSEI"  # Nifty 50 symbol on Yahoo Finance

    def fetch_data(self):
        print(f"[{self.market_name}] Fetching live data for {self.symbol}...")
        try:
            ticker = yf.Ticker(self.symbol)
            data = ticker.history(period="1d")
            current_price = data['Close'].iloc[-1]
            return {"symbol": "NIFTY 50", "price": round(current_price, 2), "rsi": 50.0}
        except Exception as e:
            print(f"Error fetching Indian market data: {e}")
            return {"symbol": "NIFTY 50", "price": 24550.25, "rsi": 50.0}

    def analyze(self, data):
        print(f"--- 🇮🇳 {self.market_name} Analysis ---")
        print(f"Asset: {data['symbol']} | Live Price: ₹{data['price']} | Status: Active Monitoring\n")


class ForexMarketBot:
    def __init__(self):
        self.market_name = "Forex Market"
        self.symbol = "USDINR=X"  # USD to INR Forex pair

    def fetch_data(self):
        print(f"[{self.market_name}] Fetching live data for {self.symbol}...")
        try:
            ticker = yf.Ticker(self.symbol)
            data = ticker.history(period="1d")
            current_price = data['Close'].iloc[-1]
            return {"symbol": "USD/INR", "price": round(current_price, 2), "rsi": 48.0}
        except Exception as e:
            print(f"Error fetching Forex data: {e}")
            return {"symbol": "USD/INR", "price": 83.42, "rsi": 48.0}

    def analyze(self, data):
        print(f"--- 🌍 {self.market_name} Analysis ---")
        print(f"Asset: {data['symbol']} | Live Price: {data['price']} | Status: Active Monitoring\n")


if __name__ == "__main__":
    print("🚀 TradePulse AI - Live Market Bot Started...\n")
    
    indian_bot = IndianMarketBot()
    forex_bot = ForexMarketBot()

    while True:
        ind_data = indian_bot.fetch_data()
        indian_bot.analyze(ind_data)

        fx_data = forex_bot.fetch_data()
        forex_bot.analyze(fx_data)

        print("="*40)
        print("Waiting 60 seconds for next live scan...\n")
        time.sleep(60)  # Har 60 seconds me live check karega
