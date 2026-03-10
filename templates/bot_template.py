from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "TOKEN"

async def start(update, context):
    await update.message.reply_text("Бот работает")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
