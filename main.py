import asyncio
from pyrogram import Client
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

app = Client("walter", api_id=API_ID, api_hash=API_HASH)

# Replace 'your_file.json' with the path to your actual JSON file
file_path = 'winners.json'

# Open the JSON file and load its content into a Python list
with open(file_path, 'r') as file:
    winners = json.load(file)


async def main():
    async with Client("walter", API_ID, API_HASH) as app:
        for winner in winners:
            await app.send_message(winner, "Greetings from **Pyrogram**!")


asyncio.run(main())
