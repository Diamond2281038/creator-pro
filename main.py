import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from config import BOT_TOKEN
from database import init_db, add_bot, get_user_bots
from bot_manager import create_bot_file, start_bot

keyboard = [
    ["Создать бота"],
    ["Мои боты"]
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤖 Creator PRO\n\nВыберите действие",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


async def text(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text
    user_id = update.message.from_user.id

    if msg == "Создать бота":
        context.user_data["create"] = True
        await update.message.reply_text("Отправь токен бота")
        return


    if msg == "Мои боты":

        bots = get_user_bots(user_id)

        if not bots:
            await update.message.reply_text("У тебя нет ботов")
            return

        text = "Твои боты:\n"

        for bot in bots:
            text += f"{bot[0]}\n"

        await update.message.reply_text(text)
        return


    if context.user_data.get("create"):

        token = msg

        file = create_bot_file(token, user_id)

        start_bot(file)

        add_bot(user_id, token, file)

        await update.message.reply_text("✅ Бот создан и запущен")

        context.user_data["create"] = False


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, text))

init_db()

print("Creator PRO started")

app.run_polling()
