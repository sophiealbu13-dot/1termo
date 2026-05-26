# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

print("Bem-vindo ao Sistema")
print("Elevador no andar: 0 (Térreo)")
andar_inicial = int(input("Qual andar você quer chamar o elevador?"))
lista = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
import time
while True:
    pessoas = int(input("Quantas pessoas vão no elevador: "))


if pessoas <=5:
    print("Quantidade de pessoas no limite")
else:
    print("Passou do limite de pessoas!")
    break

if andar_inicial == lista:
    print(f"elevador indo para o andar:{andar_inicial}")
    print("elevador chegou!")


BRUNO
print("Bem-vindo ao Elevador Python!")
andar_atual = 0 
while True:
    try:
        destino = int(input("Digite o andar de destino (0-10): "))
        if destino < 0 or destino > 10:
            raise ValueError("Andar inválido. Por favor, digite um número entre 0 e 10. ")

print(f"Elevador se movendo do andar {andar_inicial} para o andar {destino}...")
andar_atual = destino
print(f"Chegamos ao andar {andar_atual}!")

if input("Deseja escolher outro andar? (s/n): ").lower() 1=
's':
print("Obrigada por usar o Elevador Python! Até a próxima! ")
break
for listagem in range(10):
    prin(f"Andar {listagem} - {'[x]' if listagem == andar_atual else '[]'}")
