import os
import telebot
from datetime import datetime

TOKEN = os.environ.get("GadrQrfvpNeCZaWNLxpdrJYGMbsFRccQ")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply(message):
    # الوقت الحالي
    now = datetime.now()
    hour = now.hour

    # البوت يشتغل فقط من 10 صباحًا (10) حتى 11 مساءً (23)
    if 10 <= hour <= 23:
        text = message.text.lower()

        if "وش اخذنا واجب اليوم" in text:
            bot.reply_to(
                message,
                "📚 لم يتم الإعلان عن واجب أو بحث في هذا اليوم."
            )

        elif "وش علينا واجبات" in text:
            bot.reply_to(
                message,
                "✏️ اكتب هنا الرد اللي تبيه انت"
            )
    else:
        # خارج الوقت المحدد، البوت ما يرد
        pass

bot.infinity_polling()
