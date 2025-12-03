import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')


bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет,я учусь писать код!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
