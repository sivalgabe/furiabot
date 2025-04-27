from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    print("ERRO: TOKEN não foi carregado")
    exit()

print(f"TOKEN carregado: {TOKEN}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Olá, Furiose! Seja bem-vinde ao nosso chat!")

async def debug_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    text = update.message.text

    print(f"[DEBUG] Mensagem de {user}: {text}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, debug_message))

print("Furiosamente Online!")

app.run_polling()