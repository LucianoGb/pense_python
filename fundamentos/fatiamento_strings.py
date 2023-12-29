nome = 'Luciano Gouveia'
print(nome[0:7])

'''
O operador [n:m] retorna a parte da string do “enésimo” 
caractere ao “emésimo” caractere, incluindo o primeiro, mas excluindo o último.
Downey, Allen B.. Pense em Python:(p. 136) 
'''

'''
txt:    BANANA
indice: 012345
'''

fruta = 'banana'
print(f'\nfruta[:3]: {fruta[:3]}')
print(f'fruta[3:]: {fruta[3:]}')

#Se o primeiro índice for maior ou igual ao segundo, o resultado é uma string vazia, representada por duas aspas:

print(f'\nfruta[3:3]: {fruta[3:3]}')


def busca(palavra, letra): 
    index = 0 
    while index < len(palavra): 
        if palavra[index] == letra: 
            return index 
        index = index + 1 
    return -1;

retorno = busca('luciano', 'n')
print(retorno)