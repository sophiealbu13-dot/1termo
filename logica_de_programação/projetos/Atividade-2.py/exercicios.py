# Exercicio 1
# Cáculo de Notas
#Somativa 1 e Somativa 2
#Valores de 0 a 100
#O valor derevá ser atribuido por duas notas e uma média final e ao final deberá ser apresentado o resultado e uma média final e ao final deverá ser apresentado o resultado

# print ("Bem-Vindos ao calculo de Notas")
# print ("Notas do Senai")
# print ("As notas Senai")

# nota1 = float(input("Digite a somativa 1"))
# nota2 = float(input("Digite a somativa 2"))
# media = (nota1 + nota2) / 2
# print("Sua media final foi: ",round(media,2))

# Exercicio 2
# Criar um algoritimo para simular uma calculadora
# deverar conter os operadores + - / =
# Ao inserir o valor 1 e o valor 2 ela deve apresentar o resultado

# print("Calculadora de Operadores")
# print("Escolha uma das opções")
# print("Soma + ")
# print("Subtração - ")
# print("Divisão / ")
# print("Multiplicação * ")

# valor1 = float(input("Digite o primeiro valor"))
# valor2 = float(input("Digite o segundo valor"))
# operador = input("Qual operador deseja?")

# if operador == "+": 
#      soma = valor1 + valor2
#      print("A soma foi: ", soma)
# if operador == "-": 
#      soma = valor1 - valor2
#      print("A subtração foi: ", subtração)
# if operador == "/": 
#      soma = valor1 / valor2
#      print("A divisão foi: ", divisão)
# if operador == "*": 
#      soma = valor1 * valor2
#      print("A multiplicação foi: ", multiplicação)

# else:
#     print("Obrigado por usar a nossa calculadora")

# Exercicio 3
# Loja de Roupas, Sapatos e Perfumes
# Ao escolher uma das opção você deverá perguntar o valor do produto, a quantidade e aplicar desconto
# Roupas = 10%
# Sapatos = 5%
# Perfume = 2%

print("Loja de Roupas")
print("Nós trabalhamos com sapatos, roupas e perfumes")
print("Escolha uma opções para iniciar uma comprar")
print("Digite 1 para roupas")
print("Digite 2 para sapados")
print("Digite 3 para perfumes")

opção = int(input("Digite a opção desejado"))

if opção == 1: 
    print("Você escolhe o setor da Roupas")
    prod = float(input("Digite o valor do produto:"))
    qtde = int(input("Digite a quantidade "))