# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

from collections import deque
import time

# =========================
# CONFIGURAÇÕES DO ELEVADOR
# =========================
ANDAR_MIN = 0
ANDAR_MAX = 9
CAPACIDADE_MAX = 5

# =========================
# VARIÁVEIS DO SISTEMA
# =========================
andar_atual = 0
pessoas = 0
fila_chamadas = deque()

# =========================
# FUNÇÕES
# =========================

def mostrar_status():
    print("\n==============================")
    print(f"Andar atual: {andar_atual}")
    print(f"Pessoas no elevador: {pessoas}")
    print("==============================\n")


def validar_andar(andar):
    return ANDAR_MIN <= andar <= ANDAR_MAX


def mover_elevador(destino):
    global andar_atual

    while andar_atual != destino:

        if andar_atual < destino:
            andar_atual += 1
            print(f"Subindo... Andar {andar_atual}")

        elif andar_atual > destino:
            andar_atual -= 1
            print(f"Descendo... Andar {andar_atual}")

        time.sleep(0.3)

    print("Parando...")
    mostrar_status()


def embarque():
    global pessoas

    try:
        entrando = int(input("Quantas pessoas entrarão? "))

        if entrando < 0:
            print("Valor inválido.")
            return

        if pessoas + entrando > CAPACIDADE_MAX:
            print("Capacidade máxima excedida!")
        else:
            pessoas += entrando
            print(f"{entrando} pessoa(s) embarcaram.")

    except ValueError:
        print("Digite apenas números.")


def desembarque():
    global pessoas

    try:
        saindo = int(input("Quantas pessoas sairão? "))

        if saindo < 0 or saindo > pessoas:
            print("Quantidade inválida.")
        else:
            pessoas -= saindo
            print(f"{saindo} pessoa(s) desembarcaram.")

    except ValueError:
        print("Digite apenas números.")


def adicionar_chamada():
    try:
        origem = int(input("Digite o andar de origem: "))
        destino = int(input("Digite o andar de destino: "))

        if not validar_andar(origem) or not validar_andar(destino):
            print("Andar inválido! Digite valores entre 0 e 9.")
            return

        fila_chamadas.append((origem, destino))
        print("Chamada adicionada à fila.")

    except ValueError:
        print("Digite apenas números.")


def processar_fila():
    while fila_chamadas:

        origem, destino = fila_chamadas.popleft()

        print("\n===================================")
        print(f"Atendendo chamada: {origem} -> {destino}")
        print("===================================\n")

        # Vai até o andar de origem
        mover_elevador(origem)

        # Embarque
        embarque()

        # Vai até o destino
        mover_elevador(destino)

        # Desembarque
        desembarque()

        mostrar_status()


# =========================
# MENU PRINCIPAL
# =========================

while True:

    print("===== SISTEMA DE ELEVADOR =====")
    print("1 - Chamar elevador")
    print("2 - Processar chamadas")
    print("3 - Mostrar status")
    print("4 - Encerrar programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_chamada()

    elif opcao == "2":
        processar_fila()

    elif opcao == "3":
        mostrar_status()

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida.")