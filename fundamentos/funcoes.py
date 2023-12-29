# -*- coding: cp1252 -*- #usado para imprimir caracteres especiais.

# função type retorna o tipo do valor passado por parâmetro

nome = 'Luciano'

# função para imprimir valor em tela.

print(type(nome)) # retorno esperado <class 'str'>

# lista de funções para conversao de tipo

to_int = int(3.9) # irá converter o valor para inteiro
to_float = float(3) # irá converter o valor para float
to_str = str(3.9) # irá converter o valor para string

print(f'\n valor variavel: {to_int}, tipo: {type(to_int)}, função: int()')
print(f'\n valor variavel: {to_float}, tipo: {type(to_float)}, função: float()')
print(f'\n valor variavel: {to_str}, tipo: {type(to_str)}, função: str()')

# declaração de nova funções usa a palavra reservada def seguido do nome da função + () e : em seguida para indicar o bloco da função

def ola_mundo():
    print('Olá mundo')

# chamada da função

ola_mundo()   

# passagem de parâmetros

def soma(valor1, valor2):
    """
    Soma de dois valores

    Args:
        valor1 (int | float): 
        valor2 (int | float):
    """
    print(valor1 + valor2)
    
soma(10, 40) # sa�da 50

soma()
