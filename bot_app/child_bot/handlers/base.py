import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict
from aiogram import Bot, Dispatcher, F, Router, html



from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.filters import Command
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

child_bot_router = Router()


@child_bot_router.message(Command(commands=["start"]))
async def command_start(message: Message):
    await message.answer(
        "Yes, I'm a child bot and launched successfully"
    )


async def main():
    bot = Bot(token=getenv("TELEGRAM_TOKEN"), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(child_bot_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
