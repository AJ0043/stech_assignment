from telegram.ext import Updater, MessageHandler, Filters  # type: ignore

API_KEY = '7985598038:AAGKbOIE2kO3CgkQe6t4Vu8b01qA7HE-KA0'

print("✅ Telegram bot is Started.....")

def handle_message(update, context):
    text = update.message.text.lower()
    print(f"📩 Received message: {text}")
    update.message.reply_text(f"Hello {text}! How can I assist you?")

if __name__ == "__main__":
    print("🚀 Bot is launching...")  
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()


