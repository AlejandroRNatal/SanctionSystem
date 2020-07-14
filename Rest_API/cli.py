import asyncio, os, sys

async def input_loop():
    yield input("Provide name to verify sanction status:")

def main_loop():

    curr = ''
    while curr.strip() != 'quit':
        #ask our input here
        curr = await input_loop()
    return


if __name__ == "__main__":
    asyncio.run(main_loop())