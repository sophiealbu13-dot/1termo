# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diaria 
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um: 

# # Exemplo 1
# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. {OK}")
#     print("Produção do dia finalizada!")

# # Exemplo 2 
# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# # Exemplo 3 
# # Imagine o seguinte cenario, iremos produzir 20 discos de vinil.

# for disco in range(21):
#     print(f"Quantidade total {disco} produzidos foi..")

# Exemplo 4 
# peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda"]
# itempecas = ["Cilindricas", "Cônicas", "Rosca sem-fim", "planetárias", "Cremalheira",]


# for item in pecas:
#     print(f"Item em estoque: {item} e {itempecas}")

# for item2 in itempecas: 
#     print(f"Item de peças de retoque: {itempecas}")

    # Exemplo 5 
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos

# print("Loja dos Albuquerques")
# print("Opção 1- Peças")
# print("Opção 2- Item Peças")
# menu = int(input("Escolha uma opção"))

# peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo", "Prego", "Chave de Fenda"]
# itempecas = ["Cilindricas", "Cônicas", "Rosca sem-fim", "planetárias", "Cremalheira",]

# if menu == 1:
#     for item in peças:
#         print(f"Sua lista de peças {peças} são...")
# elif menu == 2: 
#     print(f"Sua lista de itens de peças {itempecas} são...")

# else:
#     print("Opção inválida: Encerrando o sistema")


# Exemplo 5 
# # 1. Contador de produção (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluido".
# for peça in range(1, 10):
#     print(f "Peça numero {peças} processada com sucesso!")
# print(Ciclo de produção concluido!)
      
    
# Exercicio 2 
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, melancia, abacaxi. Com uma quantidade de 10 banana, 5 mangas, 10 melancias e 13 abacaxi.

print("Loja dos Albuquerques")
print("Opção 1- banana = 10")
print("Opção 2- mangas = 5")
print("Opção 3- melancia = 10")
print("Opção 4- abacaxi = 13")
menu = int(input("Escolha uma opção"))

frutas = ["banana", "mangas", "melancia", "abacaxi"]

if menu == 1:
    for banana in range(1,11):
        print(f"Sua lista de frutas {banana} são...")
elif menu == 2: 
    for mangas in range(1,6):
        print(f"Sua lista de itens de frutas {mangas} são...")

elif menu == 3: 
    for melancia in range(1,11):
        print(f"Sua lista de itens de frutas {melancia} são...")

elif menu == 4: 
    for abacaxi in range(1,14):
        print(f"Sua lista de itens de frutas {abacaxi} são...")

else:
    print("Opção inválida: Encerrando o sistema")