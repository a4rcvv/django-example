import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # scope: djangoのrequestのようなもの WebSocketだと1コネクションにつき1スコープ
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # groupにchannelを追加
        # channelについてよく分かっていない
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        # ハンドシェイク承認
        await self.accept()

    async def disconnect(self, code):
        # groupからchannelを除去
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        # クライアントからデータを受信した時に呼ばれる
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # group内全てのチャンネルに対してchat_messageイベントを実行する
        await self.channel_layer.group_send(self.room_group_name, {"type": "chat_message", "message": message})

    async def chat_message(self, event):
        message = event["message"]
        # クライアントにメッセージを送信
        await self.send(text_data=json.dumps({"message": message}))
