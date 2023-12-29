# strings é uma cadeia de caracteres que podem ser acessível pelo seu índice

fruta = 'banana'

# 0=b, 1=a, 2=n, 3=a, 4=n, 5=a

print(fruta[1]) # a

# função para saber o tamanho de uma string

tamanho = len(fruta)

print(f'O tamanho da string banana é: {tamanho}')

# pegando o último indice de uma string, você pega o tamanho total e subtrai 1

ultima_letra = fruta[tamanho - 1]
print(f'A última letra é : {ultima_letra} ')

# outra forma é usar índice negativa como -i

print(f'A última letra usando índice negativo é : {fruta[-1]} ')

# algumas funções relacionado a string

fruta.capitalize() # Banana - Primeira letra maiúscula

fruta.casefold() # banana - ransforma todas as letras em minúsculas

fruta.count('a') # conta quantas vezes tem a letra 'a'

'Mario'.find('i') # procura outro texto ou parte de texto dentro da string e retorna a primeira posição.

'123'.isnumeric() # Verifica se um texto é todo feito por números;

salario = '1250,00'

salario.replace(',' , '.') # Substitui um texto por um outro texto em uma string; 1250.00

email = 'luciano@gmail.com'
email.split('@') # Separa uma string de acordo com um delimitador em vários textos diferentes;
# retorna ['luciano', 'gmail.com']

' Luciano '.strip() # retira caracteres indejados ou espaçoes extras no ínicio e fim da string
# 'Luciano'

'luciano gouveia'.title() # coloca a primeira letra de cada palavra em maiúscula

'luciano'.upper() # deixa tudo em maiúsculo.

# pecorrendo uma string com o for

for letra in fruta:
    print(letra)
    

print('a' in 'banana') # Verifica se 'a' existe em 'banana' - True

