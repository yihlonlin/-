#linebot 相關設定請複習之前上課內容
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

app = Flask(__name__)
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "Quickstart-afd884cc69c5.json", scope)
client = gspread.authorize(creds)
spreadSheet = client.open("linebottest")  # 抓取sheet表單名稱
worksheet = spreadSheet.worksheet("test1")  # sheet工作區名稱

line_bot_api = LineBotApi(
    'CW+653uc68/83bO+H1UKlYsFsD4ZdfsUCf7CciDuNmKlMV+9FsfQ84kM0El5Lxj7kfo7WuW4vMQAaDe1iZK7mKudt9pPwsAzvQtOsMLWSyi+oLVc+gbQorLrrMREFqcRqO1HhVK5PObY1xQqL1Q1SQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('681aac37aa4b961f677ffae94fb07aa6')

end = "問卷結束 等待分析結果"


def totalpoint(row_num):
    sum = 0
    for k in range(2, 8):
        a = int(worksheet.cell(row_num, k).value)
        sum = sum + a
    if sum < 5:
        return "身心適應狀況良好", sum
    if 10 > sum > 5:
        return "輕度情緒困擾，找家人或朋友談談，紓發情緒", sum
    if 14 >= sum >= 10:
        return "中度情緒困擾，建議尋求紓壓管道或接受心理專業諮詢", sum
    if sum >= 15:
        return "重度情緒困擾，建議諮詢精神科醫師接受近一步的評估", sum


# getLastrow = worksheet.row_values(1)  # 取得第一列的最後一個 紀錄last取得方式
# 以下是取得第一行的最後一個函數寫法
# def findLastRow():  # 取得第一行的最後一個
#    getlastcol = worksheet.col_values(1)
#    return len(getlastcol)


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    profile = line_bot_api.get_profile(event.source.user_id)
    clientID = profile.user_id
    getlastcol = len(worksheet.col_values(1))
    for i in range(getlastcol, 0, -1):
        # getid = worksheet.cell(i, 1).value  # 取得暫存id
        if worksheet.cell(i, 1).value == clientID:
            for j in range(2, 8, 1):
                if worksheet.cell(i, j).value == "":
                    if j == 7:
                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text=end))
                        worksheet.update_cell(i, 7, msg)
                        total = totalpoint(i)
                        line_bot_api.push_message(
                            clientID, TextSendMessage(text=total[0]))
                        worksheet.update_cell(i, 8, total[1])
                        break
                    else:
                        remsg = worksheet.cell(1, j + 1).value
                        line_bot_api.reply_message(
                            event.reply_token, TextSendMessage(text=remsg))
                        worksheet.update_cell(i, j, msg)
                        break
                elif worksheet.cell(i, 7).value != "":
                    remsg = worksheet.cell(1, 2).value
                    line_bot_api.reply_message(
                        event.reply_token, TextSendMessage(text=remsg))
                    worksheet.update_cell(getlastcol + 1, 1, clientID)
                    break
            break
        elif worksheet.cell(3, 1).value != clientID:
            remsg = worksheet.cell(1, 2).value
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text=remsg))
            worksheet.update_cell(getlastcol + 1, 1, clientID)
            break

    # another

    # try:
    #     find_id = worksheet.find(clientID)
    #     i = find_id.row
    #     for j in range(2, 8):
    #         if worksheet.cell(i, j).value == "":
    #             if j != 7:
    #                 worksheet.update_cell(i, j, msg)
    #                 remsg = worksheet.cell(1, j + 1).value
    #                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    #                 break
    #             else:
    #                 worksheet.update_cell(i, 7, msg)
    #                 line_bot_api.reply_message(event.reply_token, TextSendMessage(text=end))
    #                 total = totalpoint(i)
    #                 line_bot_api.push_message(clientID, TextSendMessage(text=total))
    #                 break
    #             break
    #         elif worksheet.cell(i, 7).value != "":
    #             getlastcol = len(worksheet.col_values(1))
    #             worksheet.update_cell(getlastcol + 1, 1, clientID)
    #             remsg = worksheet.cell(1, 2).value
    #             line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))
    #             break
    # except gspread.exceptions.CellNotFound:
    #     getlastcol = len(worksheet.col_values(1))
    #     worksheet.update_cell(getlastcol + 1, 1, clientID)
    #     remsg = worksheet.cell(1, 2).value
    #     line_bot_api.reply_message(event.reply_token, TextSendMessage(text=remsg))


if __name__ == '__main__':
    app.run(debug=True, port=80)
