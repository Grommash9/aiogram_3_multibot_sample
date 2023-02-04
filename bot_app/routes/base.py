from bot_app.misc import routes
from aiohttp import web


@routes.get('/da')
async def get_da(request):
    return web.Response(status=200, body=f"da")


@routes.post('/send_notification/')
async def send_any_notification(request):
    print(request)
    print(type(request))
    # data = await request.
    # bot_token = request.match_info['bot_token']
    # tx_data = dict(request.query)
    # user_id = tx_data['user_id']
    # message = tx_data['message']
    #
    # await Bot(bot_token).send_message(user_id, message)
    # return web.Response(status=200, body=f"hello world")

@routes.post('/')
async def send_any_notification(request):
    print(request)
    print(type(request))