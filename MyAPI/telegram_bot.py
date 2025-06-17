from telegram.ext import Updater, MessageHandler, Filters  # type: ignore

API_KEY = '7985598038:AAGKbOIE2kO3CgkQe6t4Vu8b01qA7HE-KA0'
print("✅ Telegram bot started...")

def handle_message(update, context):
    text = update.message.text
    print(update)
    
    update.message.reply_text(f"Hello {update.message.chat.first_name}")

if __name__ == "__main__":
    updater = Updater(API_KEY, use_context=True)  # type: ignore
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))  # type: ignore

    updater.start_polling()
    updater.idle()
