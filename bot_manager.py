import subprocess
import os
from config import BOTS_FOLDER

def create_bot_file(token, user_id):
    if not os.path.exists(BOTS_FOLDER):
        os.makedirs(BOTS_FOLDER)

    file = f"{BOTS_FOLDER}/bot_{user_id}.py"

    code = f'''
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "{token}"

async def start(update, context):
    await update.message.reply_text("Бот запущен")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started")
app.run_polling()
'''

    with open(file, "w") as f:
        f.write(code)

    return file


def start_bot(file):
    subprocess.Popen(["python", file])
