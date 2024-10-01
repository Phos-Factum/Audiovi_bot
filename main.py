import asyncio
import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

# Into handlers.py
from aiogram import F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

# Loading environmental variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Also into handlers.py
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello! It's a testy start of me.")


@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Help manual.")


@dp.message(F.text == "test")
async def f_test(message: Message):
    await message.answer("Test was successful!")


# Starting a bot and including router
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
