
from oauth2client.service_account import ServiceAccountCredentials
import find_data
import re
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

line_bot_api = LineBotApi(
    'CW+653uc68/83bO+H1UKlYsFsD4ZdfsUCf7CciDuNmKlMV+9FsfQ84kM0El5Lxj7kfo7WuW4vMQAaDe1iZK7mKudt9pPwsAzvQtOsMLWSyi+oLVc+gbQorLrrMREFqcRqO1HhVK5PObY1xQqL1Q1SQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('681aac37aa4b961f677ffae94fb07aa6')

app = Flask(__name__)


# line-bot 基本設定詳請可看https://github.com/line/line-bot-sdk-python
@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("Request body: " + body, "Signature: " + signature)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 機器人主要讀入傳出
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="正在查詢請稍後!"))
    profile = line_bot_api.get_profile(event.source.user_id)
    clientID = profile.user_id
    msg = event.message.text
    remsg = find_data.find_time(msg)
    if type(remsg)==list:
        for i in remsg:
            printmsg = str(i)
            me = re.sub("[.\{}''\"\"\[\]]", '', printmsg)
            line_bot_api.push_message(
                clientID, TextSendMessage(text=me))
    else:
        line_bot_api.push_message(
            clientID, TextSendMessage(text=remsg))

if __name__ == '__main__':
    app.run(debug=True, port=5042)
