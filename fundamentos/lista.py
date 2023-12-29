# Lista é um sequência de valores e pode ser de qualquer tipo

# Declaração

lista = [1,2,3]
nomes = ['Luciano', 'Lucas', 'Luan']

# Lista aninhada
lista_aninhada = ['Luciano', [10,20]]
# Lista são mutáveis

# Pecorrendo uma Lista

for item in lista:
    print(item)
    
# Pecorrendo com len e range
print('Pecorrendo com Range e Len')

for item in range(len(lista)):
    # pecorre a lista e atualiza os valores
    lista[item] = lista[item] * 2

print(f'Lista atualizada: {lista}')

# a função split, vai dividir a string pegando o texto até a vírgula do input e vai criar uma lista
encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
print(f'Encomendas: {encomendas}')

# Métodos de Lista
t = ['a', 'b', 'c', 'd']
print(f'Lista original: {t}')
# appende adiciona um novo elemento ao fim da lista
t.append('e')
print(f'Lista incrementada com append: {t}')
# extend toma uma nova lista como argumento e adiciona todos elementos
t2 = ['f','g']
print(f'nova lista: {t2}')
t.extend(t2)
print(f'Lista original icrementada usando extend e usando o valores da nova lista, o resultado é: {t}')

# sort classifica os elementos da lista em ordem ascendente
sort_list = [5, 10, 30, 1, 4 ,50]
print(f'Nova Lista para ser oganizada: {sort_list}')
sort_list.sort() # o retorno desse método é none
print(f'Lista alterada usando sort{sort_list}')

# método sum usado para somar os valores de uma lista
soma_numero = sum(sort_list)
print(f'resultado do sum: {soma_numero}')

# método pop
nova_lista = ['a', 'b', 'c', 'd']
print(f'Lista: {nova_lista}')
nova_lista.pop(2)
print(f'Lista alterada com o pop no índice 2 = c: {nova_lista}')
# altera a lista e retorna o elemento que foi excluído. Se você não incluir um índice, ele exclui e retorna o último elemento.

# método del faz a mesma coisa mas não retorna valor, apenas exclui
del nova_lista[2]
print(f'Lista alterada usando o del {nova_lista}')

# o remove passamos o valor e não o índice - o seu retorno é none

nova_lista.remove('b')
print(f'Lista: {nova_lista}')