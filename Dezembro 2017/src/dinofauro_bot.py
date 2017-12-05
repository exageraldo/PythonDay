#! python3

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

__author__ = "Victor Matheus de Castro Geraldo"
__email__ = "victormatheuscastro@gmail.com"

#####################################_LOGS_#####################################

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

###################################_SERVIÇOS_###################################

def dinofaures(texto):
    """Traduz os textos para Dinofaures"""
    flag = False
    traduzido = ""
    substituir = {
                    "b":"f", "j":"f", "p":"f", "s":"f",
                    "B":"F", "J":"F", "P":"F", "S":"F",
                    "x":"f", "v":"f", "z":"f", "ç":"f",
                    "X":"F", "V":"F", "Z":"F", "Ç":"F",
                    "ci":"fi", "ce":"fe",
                    "CI":"FI", "CE":"FE",
                    "Ci":"Fi", "Ce":"Fe"
                }
    for letra in substituir: texto = texto.replace(letra, substituir[letra])
    for letra in texto:
        verifica_f = letra.upper() == 'F'
        if verifica_f and flag == False: flag = True
        elif verifica_f and flag == True: continue
        else: flag = False
        traduzido += letra
    return(traduzido)

###################################_COMANDOS_###################################

def start(bot, update):
    """Envia a mensagem quando o comando /start é executado"""
    iniciar = (
        "Seja bem vindo!\n\n"
        "Esse é um bot desenvolvido para o Python Day Natal 2k17.\n"
        "Todas as mensagens enviadas para o bot, serão traduzidas para Dinofaures.\n"
        "Para mais informações digite /help\n"
        "Divirta-se!"
    )
    update.message.reply_text(iniciar)

def help(bot, update):
    """Envia uma mensagem de ajuda quando o comando /help é executado"""
    ajuda = (
        "Esse bot funciona somente mandando uma mensagem e traduzirá automaticamente para dinofaures\n"
        "Para mais ajuda/reclamações/sugestões, entre em contato com o desenvolvedor @exaGeraldo"
    )
    update.message.reply_text(ajuda)

def traduzir(bot, update):
    """Retorna a mensagem traduzida ao usuário"""
    texto = update.message.text
    dino = dinofaures(texto)
    update.message.reply_text(dino)

def error(bot, update, error):
    """Log de erros causados pelas atualizações"""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    updater = Updater("481907817:AAHnNTohqNpR9HEHoLVVXyVurHrtIARLQPE")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, traduzir))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
