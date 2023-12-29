# -*- coding: utf-8 -*- #usado para imprimir caracteres especiais.
import os
filmes = ['Titanic', 'Missão impossível']

def boas_vindas():
    bem_vindos = """𝓜𝔂𝓕𝓲𝓵𝓶𝓼"""
    print(len(bem_vindos) * '#')
    print(bem_vindos)
    print(len(bem_vindos) * '#')
    print('\n')
    
def exibir_menu():
    opcoes = {
        1: "Adicionar Filme",
        2: "Listar Filme",
        3: "Deletar Filme",
        4: "Sair do Sistema"
    }
    for opcao, texto in opcoes.items():
        print(f'{opcao} : {texto}')
        
    print('\n')    

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def adicionar_filme():
    filme = input('Digite o nome do filme: ')
    filmes.append(filme)
    main()
    
def listar_filmes():
    for filme in filmes:
        print(f'.{filme}')
    
    input('Aperte ENTER para voltar ao menu principal: ')
    main()

def sair():
    input('Aperte uma tecla para sair do sistema: ')
        
def escolhe_opcao():
    exibir_menu()
    try:
        opcao = int(input('\nDigite uma opção: ')) 
    
        match opcao:
            case 1:
                print('Cadastrar Filme \n')
                adicionar_filme()
            case 2:
                print('Listas de Filmes \n')
                listar_filmes()
            case 3:
                print('Deletar Filme')
            case 4:
                sair()
    except:
        opcao_invalida()
 

def main():
    os.system('cls')
    boas_vindas()
    escolhe_opcao() 
    
if __name__ == __name__:
    main()    