from typing import Union, Dict, Any
from aiogram.exceptions import TelegramUnauthorizedError
from bot_app.misc import routes, bot
from aiohttp import web
from aiohttp.web_request import Request
from aiogram.utils.token import TokenValidationError, validate_token
from aiogram import Bot
from bot_app import config


def is_bot_token(value: str) -> Union[bool, Dict[str, Any]]:
    try:
        validate_token(value)
    except TokenValidationError:
        return False
    return True


@routes.post(f'/{config.API_ROUTE_URL}/send_notification')
async def send_any_notification(request: Request):
    """
    Get the request data as a JSON object.
    Create a new instance of the Bot class with the provided bot token and session.
    Use the Bot instance to call the send_message method with the provided target chat ID and message text.
    If there is an error during the message sending process, a JSON response with the error message and
    a status code of 500 will be returned.
    If the message is sent successfully, a JSON response with the message "ok" and the JSON representation
    of the message_data object will be returned, with a status code of 200.
    """
    data = await request.json()
    try:
        message_data = await Bot(data['bot_token'], session=bot.session).send_message(data['target_chat'], data['message_text'])
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)
    return web.json_response({'error': 'ok', 'message_data': message_data.json()}, status=200)


@routes.post(f'/{config.API_ROUTE_URL}/edit_message')
async def edit_message(request: Request):
    """
    Get the request data as a JSON object.
    Create a new instance of the Bot class with the provided bot token and session.
    Use the Bot instance to call edit_message_text method with the provided message text,
     target chat ID, and message ID.
    If there is an error during the message editing process, a JSON response with the error
    message and a status code of 500 will be returned.
    If the message is edited successfully, a JSON response with the message "ok" and a status
    code of 200 will be returned.
    """
    data = await request.json()
    try:
        await Bot(data['bot_token'], session=bot.session).edit_message_text(data['message_text'], data['target_chat'], data['message_id'])
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)
    return web.json_response({'error': 'ok'}, status=200)


@routes.post(f'/{config.API_ROUTE_URL}/add_new_bot')
async def adding_new_bot(request: Request):
    """
    Get the request data as a JSON object.
    Verify that the bot token is valid using the is_bot_token function.
    Create a new instance of the Bot class with the provided bot token and session.
    Try to get the user information of the bot using new_bot.get_me().
    If the bot token is invalid, a JSON response with an error message "Invalid token"
    and a status code of 500 will be returned.
    If the bot token is valid, the function sets the bot's webhook to a URL specified in
    the config.OTHER_BOTS_URL setting, using the format config.OTHER_BOTS_URL.format(bot_token=data['bot_token']).
    The function returns a JSON response indicating success and including the bot ID and
    username with a status code of 200.
    """
    data = await request.json()
    if not is_bot_token(data['bot_token']):
        return web.json_response({'error': "Invalid token"}, status=500)
    new_bot = Bot(token=data['bot_token'], session=bot.session)
    try:
        bot_user = await new_bot.get_me()
    except TelegramUnauthorizedError:
        return web.json_response({'error': "Invalid token"}, status=500)
    await new_bot.delete_webhook(drop_pending_updates=True)
    await new_bot.set_webhook(config.OTHER_BOTS_URL.format(bot_token=data['bot_token']))
    return web.json_response({'error': "ok", "data": {'bot_id': bot_user.id, 'bot_user_name': bot_user.username}}, status=200)
