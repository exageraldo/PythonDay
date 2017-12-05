#! python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

__author__ = "Victor Matheus de Castro Geraldo"
__email__ = "victormatheuscastro@gmail.com"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    """Envia a mensagem quando o comando /start é executado"""
    update.message.reply_text('Hi!')

def help(bot, update):
    """Envia uma mensagem de ajuda quando o comando /help é executado"""
    update.message.reply_text('Help!')

def echo(bot, update):
    """Envia a mesma mensagem recebida para o usuário"""
    update.message.reply_text(update.message.text)

def error(bot, update, error):
    """Log de erros causados pelas atualizações"""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater("481907817:AAHnNTohqNpR9HEHoLVVXyVurHrtIARLQPE") # Token dado pelo BotFather
    dp = updater.dispatcher # Despachante
    dp.add_handler(CommandHandler("start", start)) # Manipulador de comandos
    dp.add_handler(CommandHandler("help", help)) # Manipulador de comandos
    dp.add_handler(MessageHandler(Filters.text, echo)) # Manipulador de mensagens
    dp.add_error_handler(error) # Manipulador de erros

    updater.start_polling() #Inicia o loop de execução do bot
    updater.idle()


if __name__ == '__main__':
    main()
