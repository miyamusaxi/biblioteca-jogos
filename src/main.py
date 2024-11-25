import time

import pyautogui as py
import random

JOGOS_CADASTRADOS = []


def clear():
    py.hotkey('ctrl', ',')


def show_jogo(jogo):
    print(f"""
    Id: {jogo['id']}
    Nome: {jogo['nome']}
    Criador: {jogo['criador']}
    Distribuidora: {jogo['distribuidora']}
    Ano de lançamento: {jogo['ano_lancamento']} 
    """)


def adicionar_jogo():
    sim = ['sim', 's']
    nao = ['não', 'n', 'nao']
    jogo = {
        'id': random.randrange(0, 8),
        'nome': None,
        'criador': None,
        'distribuidora': None,
        'ano_lancamento': None,
        'jogavel': True,
    }
    clear()
    jogo['nome'] = str(input('Informe o nome do jogo: '))
    jogo['criador'] = str(input('Informe o criador do jogo: '))
    jogo['distribuidora'] = str(input('Informe a distribuidora do jogo: '))
    jogo['ano_lancamento'] = str(input('Informe o ano de lançamento do jogo: '))
    JOGOS_CADASTRADOS.append(jogo)
    print('Jogo criado com sucesso! Deseja visualizar o jogo? Responda com sim ou não')
    ver_jogo = str(input('Visualizar jogo?')).lower()
    if ver_jogo not in nao and ver_jogo not in sim:
        print('Opção inválida, seguindo processo.')
    elif ver_jogo in sim:
        show_jogo(jogo)
        time.sleep(5)
        clear()
    elif ver_jogo in nao:
        pass


def pesquisar_jogo():
    clear()
    to_search = str(input('Pesquise pelo nome ou id de um jogo: ')).lower()
    find_game = None
    for jogo in JOGOS_CADASTRADOS:
        if jogo['id'] == to_search or jogo['nome'] == to_search:
            find_game = jogo
    if find_game:
        show_jogo(find_game)
    else:
        print('Jogo não encontrado!')


def listar_jogos():
    pass


def menu():
    opcoes_validas = [1, 2, 3, 4]
    empty_line = "*************************************************"
    while True:
        print(f"""
{empty_line}
*******BEM VINDO A SUA BIBLIOTECA DE JOGOS*******
{empty_line}
* 1. Adicionar um jogo                          *
* 2. Pesquisar por um jogo                      *
* 3. Listar todos os jogos                      *
* 4. Sair                                       *
{empty_line}
{empty_line}
{empty_line}
    """)
        opcao = int(input("Informe a opção desejada "))
        if opcao not in opcoes_validas:
            print("Opção inválida. ")
        if opcao == 1:
            adicionar_jogo()
        elif opcao == 2:
            pesquisar_jogo()
        elif opcao == 3:
            listar_jogos()
        elif opcao == 4:
            break


def main():
    menu()


if __name__ == '__main__':
    main()
