from typing import Any, Dict, Union
from bot_app import config
from aiogram.exceptions import TelegramUnauthorizedError
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram.utils.token import TokenValidationError, validate_token
from aiogram import Bot, F, Router
main_router = Router()


def is_bot_token(value: str) -> Union[bool, Dict[str, Any]]:
    try:
        validate_token(value)
    except TokenValidationError:
        return False
    return True


@main_router.message(Command(commands=["start"]))
async def start_echo_command(message: Message, command: CommandObject):
    await message.answer('hello i am mother bot')


@main_router.message(Command(commands=["add"], magic=F.args.func(is_bot_token)))
async def command_add_bot(message: Message, command: CommandObject, bot: Bot) -> Any:
    """
    Check if the provided argument is a valid bot token using is_bot_token function.
    If the argument is a valid bot token, create a new instance of the Bot class with the provided token and session.
    Get the user information for the new bot using get_me method.
    Delete the current webhook for the new bot using delete_webhook method, with drop_pending_updates set to True.
    Set the new webhook URL for the new bot using the set_webhook method, the URL will be constructed using
    config.OTHER_BOTS_URL and the provided bot token.
    Send a message to the original Telegram chat with the answer "Bot @<bot_username> successful added".
    """
    new_bot = Bot(token=command.args, session=bot.session)
    try:
        bot_user = await new_bot.get_me()
    except TelegramUnauthorizedError:
        return message.answer("Invalid token")
    await new_bot.delete_webhook(drop_pending_updates=True)
    await new_bot.set_webhook(config.OTHER_BOTS_URL.format(bot_token=command.args))
    return await message.answer(f"Bot @{bot_user.username} successful added")