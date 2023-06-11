from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, FollowEvent, UnfollowEvent
LINE_CHANNEL_ACCESS_TOKEN = "CMQeIbkd3NzFsLB9zXTSiBCTVhME4Ql4xE9gfzLVHOz/hMHTK8W9YJsGu8rUPniAdD2s/W5eTzgjXhhwcoM/EPgMrlLHa+sUeW+Fe9xRY5WnwMTDaLYlSakgXa7q/lm4T6GJGm4JJL+M/cOzOEbzHQdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "26456402fd84c054d2ab125fb5061edf"
app = Flask(__name__)
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)
header = {
    "Content_Type": "application/json",
    "Authorization": "Bearer " + LINE_CHANNEL_ACCESS_TOKEN
}
@app.route("/")
def hello_world():
    return "hello world!"
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text[::-1]))
    print("返信完了!!\ntext:", event.message.text)
if __name__ == "__main__":
    app.run(host="0.0.0.0")