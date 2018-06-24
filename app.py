from flask import Flask
from flask import request
import logging
import telegram


HOST = "https://enigmatic-dusk-86931.herokuapp.com/"

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

global bot

bot = telegram.Bot(token='556481022:AAHP-XQlHy5ymFuMG25ukb_uLvxvx7AZkAQ')

bot_name = "SpellShellBot"

@app.route('/', methods=['POST', 'GET'])
def setWebhook():
    if request.method == 'GET':
        logging.info('Hello, Telegram!')
        print("Done")
    return "OЛ, Telegram Bot!"


@app.route('/verify', methods=['POST'])
def verification():
    if request.method == "POST":
        update = telegram.update.de_json(request.get_json(force=True), bot)
        if update is None:
            return  "Show me your TOKEN please!"
        logging.info("Calling {}".format(update.message))
        handle_message(update.message)
        return 'ok'


def handle_message(msg):
    text = msg.text
    print(msg)
    bot.sendMessage(chat_id=msg.chat.id, text=text)


if __name__ == "__main__":
    s = bot.setWebhook("{}/verify".format(HOST))
    if s:
        logging.info("{} WebHook Setup Ok!".format(bot_name))
    else:
        logging.info("{} WebHook Setup Failed!".format(bot_name))
    app.run(host="0.0.0.0", debug=True)
