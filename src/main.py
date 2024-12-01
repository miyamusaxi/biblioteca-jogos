import time
import os

from utils.messages_prints import *
from utils.checkers import *


def mostrar_jogo(jogo):
    print(f"{EMPTY_LINE}\n* Id: {jogo['id']}\n* Nome: {jogo['nome']}\n* Criador: {jogo['criador']}\n* Distribuidora: {jogo['distribuidora']}\n* Ano de lançamento: {jogo['ano_lancamento']}\n{EMPTY_LINE}")


def espera_e_limpa():
    sleep()
    clear()


def opcao_invalida_erro(): 
    print(OPCAO_INVALIDA_ERRO)
    espera_e_limpa()


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def sleep():
    time.sleep(3)


def generate_id(lastId):
    if lastId is None:
        return 1
    new_id = lastId + 1
    return new_id


def find_index_jogo(jogos, id):
    for index, jogo in enumerate(jogos):
        if jogo['id'] == id:
            return index



def pesquisar_jogo(jogos, to_search):
    for jogo in jogos:
        if jogo['id'] == int(to_search) or jogo['nome'].lower() == str(to_search).lower():
            return jogo
    return None


def verifica_jogo_com_mesmo_nome(jogos, nome):
    jogo = pesquisar_jogo(jogos, nome.lower())
    if jogo:
        return True
    return False


def verifica_jogo_com_mesmo_id(jogos, id):
    jogo = pesquisar_jogo(jogos, id)
    if jogo:
        return True
    return False


def verifica_jogo_ja_foi_adicionado(jogos, jogo):
    adicionado = verifica_jogo_com_mesmo_nome(jogos, jogo['nome'].lower()) and not verifica_jogo_com_mesmo_id(jogos, jogo['id'])
    return adicionado


def montar_jogo_inicial(jogos):
    if (len(jogos) <= 0):
        return {
            'id': generate_id(None),
        }
    lastId = jogos[-1]['id']
    return {
        'id': generate_id(lastId),
    }


def adicionar_jogo_menu(jogos):
    clear()
    tamanho_inical = len(jogos)
    print(CADASTRO_JOGOS_HEADER)

    jogo = montar_jogo_inicial(jogos)
    jogo['nome'] = str(input('* INFORME O NOME DO JOGO: '))
    jogo['criador'] = str(input('* INFORME O CRIADOR DO JOGO: '))
    jogo['distribuidora'] = str(input('* INFORME A DISTRIBUIDORA DO JOGO: '))
    jogo['ano_lancamento'] = str(input('* INFORME O ANO DE LANÇAMENTO DO JOGO: '))

    adicionar_jogo(jogos, jogo)

    if (len(jogos) > tamanho_inical):
        print(CADASTRO_JOGOS_SUCESSO)
        ver_jogo = str(input())
        if ver_jogo not in OPCOES_VALIDAS_SIM_OU_NAO:
            opcao_invalida_erro()
            return
        if ver_jogo in SIM:
            mostrar_jogo(jogo)
            espera_e_limpa()
            return
        clear()

def editar_jogo_menu(jogos, jogo):
    clear()
    print(EDICAO_JOGOS_HEADER)

    jogo['nome'] = str(input('* ALTERE NOME DO JOGO: '))
    jogo['criador'] = str(input('* ALTERE O CRIADOR DO JOGO: '))
    jogo['distribuidora'] = str(input('* ALTERE A DISTRIBUIDORA DO JOGO: '))
    jogo['ano_lancamento'] = str(input('* ALTERE O ANO DE LANÇAMENTO DO JOGO: '))

    adicionar_jogo(jogos, jogo)

    print(EDICAO_JOGOS_SUCESSO)
    ver_jogo = str(input())
    if ver_jogo not in OPCOES_VALIDAS_SIM_OU_NAO:
        opcao_invalida_erro()
        return
    if ver_jogo in SIM:
        mostrar_jogo(jogo)
        espera_e_limpa()
        return
    clear()


def adicionar_jogo(jogos, jogo):
    if verifica_jogo_com_mesmo_id(jogos, jogo['id']):
        index = find_index_jogo(jogos, jogo['id'])
        jogos[index] = jogo
        return
    if verifica_jogo_ja_foi_adicionado(jogos, jogo):
        print(CADASTRO_JOGOS_ERRO)
        espera_e_limpa()
        return

    jogos.append(jogo)


def pesquisar_jogo_menu(jogos):
    clear()
    print(PESQUISA_JOGOS_HEADER)
    to_search = input()
    jogo_encontrado = pesquisar_jogo(jogos, to_search)
    while jogo_encontrado is None:
        print(PESQUISA_JOGOS_ERRO)
        pesquisar = input()
        if pesquisar not in OPCOES_VALIDAS_SIM_OU_NAO:
            opcao_invalida_erro()
            break
        if pesquisar in SIM:
            print(PESQUISA_JOGOS_POR)
            to_search = input()
            jogo_encontrado = pesquisar_jogo(jogos, to_search)
    print(PESQUISA_DESEJA_EDITAR_JOGO)
    editar = input()
    if editar not in OPCOES_VALIDAS_SIM_OU_NAO:
        opcao_invalida_erro()
        return
    if editar in SIM:
        editar_jogo_menu(jogos, jogo_encontrado)
        return
    mostrar_jogo(jogo_encontrado)
    espera_e_limpa()



def listar_jogos(jogos):
    clear()
    if len(jogos) <= 0:
        print(LISTAGEM_JOGOS_ERRO_NENHUM_JOGO)
        espera_e_limpa()
        return
    print(LISTAGEM_JOGOS_HEADER)
    for jogo in jogos:
        print(f"ID : {jogo['id']} | NOME: {jogo['nome']} | LANÇAMENTO: {jogo['ano_lancamento']}")
    print(LISTAGEM_JOGOS_EDITAR)
    editar = str(input())
    if editar not in OPCOES_VALIDAS_SIM_OU_NAO:
        opcao_invalida_erro()
        return
    if editar in SIM:
        print(PESQUISA_JOGOS_POR)
        to_search = input()
        jogo = pesquisar_jogo(jogos, to_search)
        editar_jogo_menu(jogos, jogo)
    espera_e_limpa()


def menu(jogos):
    while True:
        print(MENU)
        opcao = int(input())
        if opcao not in OPCOES_VALIDAS_MENU:
            opcao_invalida_erro()
        if opcao == 1:
            adicionar_jogo_menu(jogos)
        elif opcao == 2:
            pesquisar_jogo_menu(jogos)
        elif opcao == 3:
            listar_jogos(jogos)
        elif opcao == 4:
            break


def main():
    jogos = []
    menu(jogos)


if __name__ == '__main__':
    main()
