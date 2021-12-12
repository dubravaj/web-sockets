# methods for handling different client requests
import re
from datetime import datetime
import yfinance as yf

msg_types = {
    "time": re.compile("time"),
    "stock": re.compile("stock \$[A-Z]+")
}


async def _get_current_time() -> str:
    """Get current time from server"""
    curent_time = datetime.now()
    return curent_time.strftime("%Y-%m-%d %H:%M:%S")

async def _get_stock_data(request: str):
    """Get stock data info"""
    _, ticker = request.split()
    ticker = ticker[1:]
    stock_data = yf.Ticker(ticker)
    return str(stock_data.info)


async def handle_request(request: str):
    """Handle request"""
    if re.findall(msg_types.get("time"), request):
        return await _get_current_time()
    if re.findall(msg_types["stock"], request):
        return await _get_stock_data(request)
    return ""
