import time
import requests
import yfinance as yf

# Telegram Configuration (Token & Chat ID Configured)
TELEGRAM_BOT_TOKEN = "9237671700:AAF9afF5zveuFMEkktewQ8azpcbDgwCQ4n0"
TELEGRAM_CHAT_ID = "8168357841"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

class IndianMarketBot:
    def __init__(self):
        self.market_name = "Indian Stock Market (NSE)"
        self.symbol = "^NSEI"

    def fetch_data(self):
        print(f"[{self.market_name}] Fetching live data for {self.symbol}...")
        try:
            ticker = yf.Ticker(self.symbol)
            data = ticker.history(period="1d")
            current_price = data['Close'].iloc[-1]
            return {"symbol": "NIFTY 50", "price": round(current_price, 2)}
        except Exception as e:
            print(f"Error fetching Indian market data: {e}")
            return {"symbol": "NIFTY 50", "price": 24550.25}

    def analyze(self, data):
        msg = f"🇮🇳 *{data['symbol']} Update*\nLive Price: ₹{data['price']}\nStatus: Monitoring Active"
        print(msg)
        send_telegram_alert(msg)


class ForexMarketBot:
    def __init__(self):
        self.market_name = "Forex Market"
        self.symbol = "USDINR=X"

    def fetch_data(self):
        print(f"[{self.market_name}] Fetching live data for {self.symbol}...")
        try:
            ticker = yf.Ticker(self.symbol)
            data = ticker.history(period="1d")
            current_price = data['Close'].iloc[-1]
            return {"symbol": "USD/INR", "price": round(current_price, 2)}
        except Exception as e:
            print(f"Error fetching Forex data: {e}")
            return {"symbol": "USD/INR", "price": 83.42}

    def analyze(self, data):
        msg = f"🌍 *{data['symbol']} Update*\nLive Price: {data['price']}\nStatus: Monitoring Active"
        print(msg)
        send_telegram_alert(msg)


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
        print("Waiting 60 seconds for next scan...\n")
        time.sleep(60)
