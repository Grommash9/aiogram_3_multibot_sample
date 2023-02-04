from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
)

child_bot_router = Router()


@child_bot_router.message(Command(commands=["start"]))
async def command_start(message: Message):
    await message.answer(
        "Yes, I'm a child bot and launched successfully"
    )

