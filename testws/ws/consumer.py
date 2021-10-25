from channels.generic.websocket import AsyncJsonWebsocketConsumer
from random import randint
import json
from asyncio import sleep

class WSConsummer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print(self)
        await self.accept()
        # await self.channel_layer.group_add("users", self.channel_name)
        # self.user = self.scope["user"]
        data = [{'id':1,'cointype':'BTC/USDT','value': randint(1,100)},{'id':2,'cointype':'ETH/USDT','value': randint(1,100)},{'id':3,'cointype':'Doge/USDT','value': randint(1,100)}]
        while True:
            await self.send(json.dumps(data))
            await sleep(5)
    async def receive_json(self,context):
        data = json.loads(context)
        print(data)