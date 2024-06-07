import logging
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

"""
    Task: Create a Telegram bot using the Python-telegram-bot
    library that returns information about public holidays in a given country.
    Use a public API like Calendarific for fetching the data.
    The bot should respond to the /holiday <country_code> command and return the upcoming
    public holidays in the specified country.

    Steps:
        Set up the bot and handle the /holiday command.
        Fetch public holiday data using the Calendarific API.
        Return the holiday information in a user-friendly message.

"""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

ICALENDAR_API_KEY = 'ICALENDAR_API_KEY'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Use /holiday <country_code> to get public holidays.')


def holiday(update: Update, context: CallbackContext) -> None:
    if len(context.args) != 1:
        update.message.reply_text('Usage: /holiday <country_code>')
        return

    country_code = context.args[0].upper()
    year = 2024
    api_url = f'https://calendarific.com/api/v2/holidays?&api_key={ICALENDAR_API_KEY}&country={country_code}&year={year}'

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code != 200 or data['meta']['code'] != 200:
            update.message.reply_text('Sorry, could not fetch holiday data.')
            return

        holidays = data['response']['holidays']
        if not holidays:
            update.message.reply_text('No holidays found for this country.')
            return

        holiday_info = ''
        for holiday in holidays:
            name = holiday['name']
            description = holiday['description']
            date = holiday['date']['iso']
            holiday_info += f'*{name}*\n{description}\nDate: {date}\n\n'

        update.message.reply_text(holiday_info, parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        logger.error(f"Error fetching holiday data: {e}")
        update.message.reply_text('An error occurred while fetching holiday data.')


def main() -> None:

    updater = Updater('TELEGRAM_TOKEN')

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("holiday", holiday))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
