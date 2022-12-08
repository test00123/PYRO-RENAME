from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB
from aiohttp import web
from os import environ 
PORT = environ.get("PORT", "8080")


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.mention = me.mention
       self.username = me.username 
       app = web.AppRunner(await web_server())
       await app.setup()
       bind_address = "0.0.0.0"
       await web.TCPSite(app, bind_address, PORT).start()

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

routes = web.RouteTableDef()
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("testbot")


       self.force_channel = FORCE_SUB
       if FORCE_SUB:
         try:
            link = await self.export_chat_invite_link(FORCE_SUB)                  
            self.invitelink = link
         except Exception as e:
            print(f"{e}")
            print("Make Sure Bot admin in force sub channel")             
            self.force_channel = None
       print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
       
    async def stop(self, *args):
      await super().stop()      
      print("Bot Stopped")
        
bot = Bot()
bot.run()
