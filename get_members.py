import csv
import asyncio
from pyrogram import Client, errors
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')


async def main():

    async with Client("walter", API_ID, API_HASH) as app:
        chat = await app.get_chat("Festiva XVII Group chat 🎶🎷🎻")
        print(chat)
        # for member in app.get_chat_members(chat_id):
        #     print(member)


asyncio.run(main())
