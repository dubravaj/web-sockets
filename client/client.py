#!/user/bin/env python
# Example of websockets client using Python, asyncio library
import logging
import asyncio
import websockets

class WebsocketClient:
    """Example of websockets client"""

    def __init__(self, host: str ="localhost", port: int = 8765) -> None:
        self.host = host
        self.port = str(port)
        self.logger = logging.getLogger("websockets-client")

    async def connect(self):
        """Create connection to server"""
        async with websockets.connect(f"ws://{self.host}:{self.port}") as websocket:
            await websocket.send("hello from client")
            response = await websocket.recv()
            print(f"{response}")
            
    
if __name__ == "__main__":
    client = WebsocketClient()
    asyncio.run(client.connect())


