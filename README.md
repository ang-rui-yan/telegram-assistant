# Telegram Assistant

This script uses Telegram Selfbot to blast messages on your behalf.

## Steps

1. Obtain your Telegram API.

   Access the following [link](https://core.telegram.org/api/obtaining_api_id) and follow the steps to get your API ID and API Hash.

1. Create a virtual environment

   ```
   pip install virtualenv
   virtualenv venv
   ```

   For macOS

   ```
   source ./venv/bin/activate
   ```

   For Windows

   ```
   cd venv/bin
   activate.bat
   ```

1. Install the requirements into your virtual environment

   ```
   pip install -r requirements.txt
   ```

1. Create a copy of .example(s)

   ```
   cp .env.example .env
   cp winners.csv.example winners.csv
   ```

1. Update the API keys in your .env

   > Note: These ID and Hashs are yours only and should NOT be shared with anyone else. Keep it as a secret. There will be a .session file generated that has to be kept safe too.

1. Add in the winners into `winners.csv`

   It is to be in a single column with no headers.

1. To run it, just run `main.py`
