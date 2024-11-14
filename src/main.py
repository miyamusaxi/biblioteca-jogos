import pyautogui as py
import random

JOGOS_CADASTRADOS = []


def clear():
    py.hotkey('ctrl', ',')


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
        print(jogo)
    elif ver_jogo in nao:
        pass


def menu():
    opcoes_validas = [1, 2, 3, 4]
    empty_line = "*************************************************"
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
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass


def main():
    menu()


if __name__ == '__main__':
    main()
