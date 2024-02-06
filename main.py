import csv
import asyncio
from pyrogram import Client, errors
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

file_path = 'winners.csv'

with open(file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    data = [row[0] for row in reader]

unreachable_users = []

with open('message.txt', 'r', encoding='utf-8') as file:
    message = file.read()


async def main():
    async with Client("walter", API_ID, API_HASH) as app:
        for winner in data:
            try:
                await app.send_message(winner, f"Hey {winner}!\n\n" + message)
            except (errors.UsernameNotOccupied, errors.PeerIdInvalid, errors.UsernameInvalid) as e:
                print(f"Error with {winner}: {str(e)}")
                unreachable_users.append(winner)
            except Exception as e:
                print(f"An unhandled error occurred: {e}.")


asyncio.run(main())

# Write the unreachable users to a file
with open('unreachable_users.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for user in unreachable_users:
        writer.writerow([user])
