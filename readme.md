# Oktoberfest Countdown Bot

This code is a Python script that generates a countdown message for the Oktoberfest event. It sends the message to a specified webhook URL using the Discord API. The message includes the remaining days, hours, and minutes until Oktoberfest, as well as a random music suggestion.

## Configuration

Before running the code, you need to set up the following configuration variables:

- `BOT_WEBHOOK`: The Discord bot webhook URL where the message will be sent.
- `OKTOBERFEST_DATE`: The date of the Oktoberfest event in the format specified by `DATE_FORMAT`.
- `DATE_FORMAT`: The format of the date used in `OKTOBERFEST_DATE`. It should follow the Python `datetime` module's date format conventions.
- `BOT_USERNAME`: The desired username for the bot that sends the message.
- `BOT_AVATAR`: The URL of the bot's avatar image.

These variables can be set either as environment variables or by creating a `.env` file in the same directory as the script. The `.env` file should have the following format:

```plaintext
BOT_WEBHOOK=<your webhook URL>
OKTOBERFEST_DATE=<date of Oktoberfest>
DATE_FORMAT=<date format> 
BOT_USERNAME=<bot username>
BOT_AVATAR=<bot avatar URL>
```

Make sure to replace the placeholders with your actual values.
For example, a right way to define these variables is:

```plaintext
BOT_WEBHOOK='https://discord.com/api/webhooks/<URI_OF_YOUR_BOT>'
BOT_USERNAME='Tage Bis Zum Oktoberfest'
BOT_AVATAR='https://i.imgur.com/HDmv45t.png'
OKTOBERFEST_DATE='2023-10-12'
DATE_FORMAT='%Y-%m-%d'
```

## Message and Music Configuration

This code uses two JSON files, `messages.json` and `musics.json`, to provide a variety of messages and music suggestions for the countdown message. 

### `messages.json`

The `messages.json` file contains a collection of messages that will be randomly selected for the countdown message. Each message in the file should have the following structure:

```json
{
  "message": "Your message goes here"
}
```

You can add or remove messages from the file to customize the content of the countdown message. The selected message will be formatted with the remaining time until Oktoberfest, which includes the number of days, hours, and minutes.

### `musics.json`

The `musics.json` file contains a collection of music suggestions that will be randomly selected for the countdown message. Each music suggestion in the file should have the following structure:

```json
{
  "music": "Your music suggestion goes here"
}
```

You can add or remove music suggestions from the file to provide a variety of music options. The selected music suggestion will be included in the countdown message along with the remaining time until Oktoberfest.

Please make sure that the JSON files (`messages.json` and `musics.json`) are located in the same directory as the Python script (`<script_name>.py`). This allows the script to read the files and retrieve the messages and music suggestions correctly.

Feel free to modify the contents of these JSON files to personalize the messages and music suggestions according to your preferences.

## Dependencies

This script requires the following Python libraries:

- `requests`: Used for making HTTP requests to the Discord API.
- `dotenv`: Used for loading environment variables from the `.env` file.
- `json`: Used for reading JSON files containing messages and music suggestions.

You can install these dependencies using pip:

```
pip install requests dotenv
```

## Running the Code

To run the code, execute the Python script using the following command:

```
python main.py
```

The script will generate a countdown message and send it to the specified Discord webhook URL. The message will include the remaining time until Oktoberfest and a random music suggestion.

Please note that you need a valid Discord webhook URL for the message to be sent successfully.