# -*- coding: cp1252 -*- #usado para imprimir caracteres especiais.

def contagem_regressiva(numero):
    if numero <= 0:
        print('Fim da execução')
    else:
        print(numero)
        contagem_regressiva(numero - 1)
        
contagem_regressiva(10)