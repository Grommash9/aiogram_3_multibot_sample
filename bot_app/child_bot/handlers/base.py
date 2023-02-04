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

