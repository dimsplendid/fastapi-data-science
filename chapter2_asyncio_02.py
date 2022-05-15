import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')

# Create event loop, excute coroutines and return its results.
asyncio.run(main())