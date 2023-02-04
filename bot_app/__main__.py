from aiogram.webhook.aiohttp_server import (
    setup_application,
)
from aiohttp import web
from bot_app import config
from bot_app import misc


def main():
    misc.app.add_routes(misc.routes)
    setup_application(misc.app, misc.main_dispatcher, bot=misc.bot)
    setup_application(misc.app, misc.multibot_dispatcher)
    web.run_app(misc.app, host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)


if __name__ == "__main__":
    main()
