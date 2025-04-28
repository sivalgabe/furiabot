from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

import os
import logging
from dotenv import load_dotenv
import respostas
import menustrings

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
    print(f"Recebi um /start de {update.effective_user.first_name}")

    keyboard = [
        [menustrings.menu_historia, menustrings.menu_titulos],
        [menustrings.menu_elenco, menustrings.menu_transf],
        [menustrings.menu_jogos, menustrings.menu_result],
        [menustrings.menu_links, menustrings.menu_furia]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def send_main_menu(update: Update):
    keyboard = [
        [menustrings.menu_historia, menustrings.menu_titulos],
        [menustrings.menu_elenco, menustrings.menu_transf],
        [menustrings.menu_jogos, menustrings.menu_result],
        [menustrings.menu_links, menustrings.menu_furia]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Escolhe uma opção por favooooor:",
        reply_markup=reply_markup
    )

async def debug_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    text = update.message.text

    print(f"[DEBUG] Mensagem de {user}: {text}")
    
    if text == menustrings.menu_historia:
        await update.message.reply_text(respostas.resposta_historia)
        await update.message.reply_text(respostas.historia_time)
    elif text == menustrings.menu_titulos:
        await update.message.reply_text(respostas.resposta_titulos)
        await update.message.reply_text(respostas.titulos)
    elif text == menustrings.menu_elenco:
        await update.message.reply_text(respostas.resposta_elenco)
        await update.message.reply_text(respostas.elenco)
    elif text == menustrings.menu_transf:
        await update.message.reply_text(respostas.resposta_transf)
        await update.message.reply_text(respostas.transferencias)
    elif text == menustrings.menu_jogos:
        await update.message.reply_text(respostas.resposta_jogos)
        await update.message.reply_text(respostas.proximos_jogos)
    elif text == menustrings.menu_result:
        await update.message.reply_text(respostas.resposta_result)
        await update.message.reply_text(respostas.resultados)
    elif text == menustrings.menu_links:
        await update.message.reply_text(respostas.resposta_links)
        await update.message.reply_text(respostas.links)
    elif text == menustrings.menu_furia:
        await update.message.reply_animation("https://media1.tenor.com/m/8gb7Dcwb6jMAAAAd/furiacs-furia.gif")
    elif text == menustrings.menu_oi:
        await update.message.reply_text(respostas.oi)
        await send_main_menu(update)
    else:
        await update.message.reply_text(respostas.tente_novamente)
        await send_main_menu(update)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, debug_message))

print("Furiosamente Online!")

app.run_polling()