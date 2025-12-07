import asyncio
import os

from aiogram import Bot, Dispatcher, F, html, types
from aiogram.enums import ParseMode
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters.command import Command, CommandObject
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

TEXT = (
    '/start - Старт Бота\n'
    '/help - помощь в навигации\n'
    '/text - проба с форматом текста\n'
    '/test_args - пробую с аргументами\n'
    '/sticker - отправлю стикер\n'
    '/emoji - отправляет дайсэмоджи футбол\n'
)

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(
        'Привет ✋,я учусь писать код!'
    )
    await message.answer(
        f'Тебя зовут, {html.bold(message.from_user.full_name)}!\n'
        'Вот мои команды',
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        TEXT
    )

@dp.message(Command('emoji'))
async def emoji_command(message: types.Message):
    await message.answer_dice(emoji='🏀')


@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.reply(TEXT)


@dp.message(Command('sticker'))
async def sticker_command(message: types.Message):
    await message.answer_sticker(
        'CAACAgIAAxkBAAEP9PdpNdyTQBBwwilUQ19zMwcHYH1OZQACHgADwDZPE6FgWy2rAAHeBDYE'
    )
    await message.answer_sticker(
        'CAACAgIAAxkBAAEP7fNpMBgks7-TILylrklmj7vxzyocswACFQADwDZPE81WpjthnmTnNgQ'
    )


@dp.message(F.text, Command('text'))
async def text_command(message: types.Message):
    await message.answer(
        '<i>Я курсивный</i>\n'
        '<b>А я жирный</b>',
        parse_mode=ParseMode.HTML
    )
    await message.answer(
        '||Я спойлер\!||\n'
        '~А я зачеркнут~',
        parse_mode=ParseMode.MARKDOWN_V2
    )


@dp.message(Command('test_args'))
async def test_args_command(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.answer('Вы не передали аргументы')
        return

    try:
        name, age, city = command.args.split(' ')
    except ValueError:
        await message.answer(
            'Введены не все аргументы. Пример ввода: \n'
            '/test_args name, age, city'
        )
        return

    await message.answer(
        f'Ваше имя: {name}\n'
        f'Ваш возраст: {age}\n'
        f'Ваш город: {city}\n'
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
