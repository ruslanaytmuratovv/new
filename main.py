import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import os
from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv("TOKEN=7646505365:AAFVHoR4fam1BrW360Vav2-3rfUXwwZK5vg")
bot = Bot(token=TOKEN)

dp = Dispatcher()
@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f"hello {message.from_user.first_name}")
@dp.message(Command('help'))
async def help(message:Message):
    await message.answer('help ne jardem kerak')
#2
@dp.message(Command('conatct'))
async def help(message:Message):
    await message.answer('comn')
#3
@dp.message(Command('admin'))
async def help(message:Message):
    await message.answer('admin')
#4
@dp.message(Command('abaut'))
async def help(message:Message):
    await message.answer('abaud')
#5
@dp.message(Command('gmail'))
async def help(message:Message):
    await message.answer('gmail ne jardem')






async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


