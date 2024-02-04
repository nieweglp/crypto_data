import asyncio
import websockets
from time import time


async def main():
    async with websockets.connect("wss://ws.blockchain.info/inv") as client:
        print("[main] Connected to wss://ws.blockchain.info/inv")

        cmd = '{"op": "unconfirmed_sub"}'
        print("[main] Send:", cmd)
        await client.send(cmd)
        response = await client.recv()
        print("[main] Recv:", response)

        with open(f"data/blockchain_{time()}.json", "w") as json_file:
            json_file.write(response)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
