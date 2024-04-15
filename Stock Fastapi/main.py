from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

ALPHA_VANTAGE_API_KEY = "4CB4EU4HMKRT2KP2"
ALPHA_VANTAGE_BASE_URL = "https://www.alphavantage.co/query"


@app.get("/stock/quote/SBIN")
async def get_stock_quote(symbol: str):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()
    if "Global Quote" not in data:
        raise HTTPException(status_code=404, detail="Stock symbol not found")
    return data["Global Quote"]


@app.get("/stock/history/SBIN")
async def get_stock_history(symbol: str, interval: str = "daily", outputsize: str = "compact"):
    params = {
        "function": "TIME_SERIES_INTRADAY" if interval == "intraday" else "TIME_SERIES_DAILY",
        "symbol": symbol,
        "interval": interval,
        "outputsize": outputsize,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()
    if "Time Series (Daily)" not in data and "Time Series (" + interval.capitalize() + ")" not in data:
        raise HTTPException(status_code=404, detail="Stock symbol not found or invalid interval")
    return data


@app.get("/stock/company/SBIN")
async def get_company_info(symbol: str):
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_BASE_URL, params=params)
    data = response.json()
    if not data:
        raise HTTPException(status_code=404, detail="Company information not found")
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
