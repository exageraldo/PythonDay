#! python3

import sys

__author__ = "Victor Matheus de Castro Geraldo"
__email__ = "victormatheuscastro@gmail.com"

def traduzir(texto):
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

if __name__ == '__main__':
    texto = " ".join(sys.argv[1:])
    print(traduzir(texto))
