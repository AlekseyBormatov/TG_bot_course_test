import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

TEXT = (
    '/start - Старт Бота\n'
    '/help - помощь в навигации'
)

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer('Привет,я учусь писать код!')

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.reply(TEXT)

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
