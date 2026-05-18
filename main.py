import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


bot = Bot(token='_TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello!")
    await message.reply("Reply")

@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("You clicked help button")


@dp.message(Command('dice'))
async def cmd_help(message: Message):
    await message.answer_dice()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("Bot stopped")
