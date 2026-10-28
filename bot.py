import time

class IndianMarketBot:
    def __init__(self):
        self.market_name = "Indian Stock Market (NSE/BSE)"

    def fetch_data(self):
        # Yahan Indian market ka live data fetch hoga (Jaise Nifty, BankNifty)
        print(f"[{self.market_name}] Fetching live indices data...")
        return {"symbol": "NIFTY 50", "price": 24550.25, "rsi": 42.5}

    def analyze(self, data):
        print(f"--- 🇮🇳 {self.market_name} Analysis ---")
        price = data["price"]
        rsi = data["rsi"]
        
        signal = "HOLD"
        if rsi < 40:
            signal = "BUY (Support Level / Oversold)"
        elif rsi > 60:
            signal = "SELL (Resistance Level / Overbought)"
            
        print(f"Asset: {data['symbol']} | Price: {price} | RSI: {rsi} | Signal: {signal}\n")


class ForexMarketBot:
    def __init__(self):
        self.market_name = "Forex Market (Global)"

    def fetch_data(self):
        # Yahan Forex market ka live data fetch hoga (Jaise EUR/USD, USD/INR)
        print(f"[{self.market_name}] Fetching live forex pairs data...")
        return {"symbol": "USD/INR", "price": 83.42, "rsi": 38.1}

    def analyze(self, data):
        print(f"--- 🌍 {self.market_name} Analysis ---")
        price = data["price"]
        rsi = data["rsi"]
        
        signal = "HOLD"
        if rsi < 40:
            signal = "BUY (Bullish Reversal Zone)"
        elif rsi > 60:
            signal = "SELL (Bearish Reversal Zone)"
            
        print(f"Asset: {data['symbol']} | Price: {price} | RSI: {rsi} | Signal: {signal}\n")


if __name__ == "__main__":
    print("🚀 TradePulse AI - Dual Market Bot Started...\n")
    
    # Dono markets ke alag objects (compartments) bana liye
    indian_bot = IndianMarketBot()
    forex_bot = ForexMarketBot()

    while True:
        # 1. Indian Market Compartment
        ind_data = indian_bot.fetch_data()
        indian_bot.analyze(ind_data)

        # 2. Forex Market Compartment
        fx_data = forex_bot.fetch_data()
        forex_bot.analyze(fx_data)

        print("="*40)
        print("Waiting for next market scan (10 seconds)...\n")
        time.sleep(10)
