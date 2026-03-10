from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from config import BOT_TOKEN
from database import init_db
from stats import get_stats

keyboard = [
    ["Создать бота"],
    ["Мои боты"],
    ["Баланс"],
    ["Статистика"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Creator PRO",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text

    if msg == "Статистика":

        users, bots = get_stats()

        await update.message.reply_text(
            f"Users: {users}\nBots: {bots}"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, text))

init_db()

print("Creator PRO started")

app.run_polling()
