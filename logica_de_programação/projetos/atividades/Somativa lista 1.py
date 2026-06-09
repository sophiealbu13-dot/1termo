1.
print ("Bem-Vindos ao jogo! ")
nome = print(input("Digite seu nick: "))
nível = print(input("Digite seu nível: "))
print("O jogador esta pronto para partida!")

2.

dinheiro = float(input("Digite a quantidade que você ganha por semana: "))
print("Por mês você ganha: ",dinheiro * 4)

3.
print("Conversão de GB pra MB")
GB = float(input("Digite o valor a quantidade desejada de GB"))
MB = float(input("Digite o valor de MB"))

multiplicação = GB * MB 
print("A quantidade de MB desejada é:", multiplicação)

4.
matematica = float(input("Digite sua nota de matematica"))
português = float(input("Digite sua nota de português"))
media = (matematica + português) / 2
print("Sua media final foi: ",round(media,2))

5.
seguidores = int(input("Digite a quantidade de seguidores atuais que você tem: "))
novos = int(input("Digite a quantidade de seguidores novos: "))
total = seguidores + novos
print("Hoje você ganhou:", total, "seguidores")

6.
idade = int(input("Digite sua idade"))
print("Você viveu:", idade * 365, "dias")

7.
salgado = int(input("Digite o preço do salgado: "))
refrigerante = int(input("Digite o preço do refrigerante: "))
total = salgado + refrigerante 
print("Total da compra foi: ", total)

8.
ano = int(input("Em que ano está: "))
idade = int(input("Quantos anos você tem: "))
total = ano - idade 
print("Você nasceu em: ", total)

9.
idade = int(input("Digite a idade do usuario: "))
if idade <= 13: 
    print("Acesso restrito!")
elif 13 < idade < 18:
    print("Acesso moderado!")
else:
    print("Acesso liberado!")

10.
import time 
bateria = 100 
while bateria < 110:
    if bateria > 10:
         print(f"A bateria esta com {bateria}%")
         bateria -= 10 
         time.sleep(1)
    elif bateria <= 10:
         print("Por favor, conecte no carregador!")
         break
else:
     print("Fim")
    
11.
Curtidas = [1, 2, 3, 4 , 5]
for likes in curtidas: 
    if likes != 6: 
        print(f"Quantidade de curtidas: {likes}")

12.
itens = ["item 1", "item 2", "item 3", "item 4", "item 5"]

