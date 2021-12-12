#!/user/bin/env python
# Example of websockets server using Python, asyncio library
import logging
from datetime import datetime
import asyncio
import websockets

logging.basicConfig(
    format="%(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG
)

class WebsocketServer:
    """Example of websockets server"""

    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = str(port)
        self.logger = logging.getLogger("websocket-server")

    async def reply(self, websocket):
        """Send reply to the client"""
        async for message in websocket:
            self.logger.info("Incoming message: %s", message)
            await websocket.send(message)

    def _get_current_time(self) -> str:
        """Get current time from server"""
        curent_time = datetime.now()
        return curent_time.strftime("%Y-%m-%d %H:%M:%S")


    async def run(self):
        """Run server"""
        async with websockets.serve(self.reply, self.host, self.port):
            self.logger.info("Server has started...")
            await asyncio.Future()

if __name__ == "__main__":
    server = WebsocketServer()
    asyncio.run(server.run())