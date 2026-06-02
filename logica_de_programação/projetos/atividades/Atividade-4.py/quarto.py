# # 2. O laço white (Repetições Inderterminadas)
# # Use o whitw quando você não sabe quando voo parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop infinito Controlado)
# Repete enquanto a temperatura estiver segura 
# Inicio

# import time 
# temperatura = 30 
# while temperatura < 80:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
# temperatura += 3 Simulando o aquecimento da máquina
# print("ALERTA! Tempuratura atingia o limite. Desligando o motor...")
# Lista de temperaturas lidas pelo sensor por minuto

# Exemplo 2: Monitoramento de temperatura com Lista de Leituras 
# Lista de Temperaturas lida pelo sensor por minuto

# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência. ")
#         break # O loop para aqui e NÃO lê os próximo valores (85, 80)
#     print(f"Temperatura está em {temp}°C. Operação normal. ")

# print("Sistema desligado. Aguardando manutenção.")


# Exemplo 3 
# materiais = ["metal", "metal", "plastico","metal", "vidro", "metal",]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peca de {peca} detectada. desviando para descarte...")
#         continue #Pula o restante do código abaixo e vai para próxima peça
#     #Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando o políndo...")

# print("Fim do lote de produção. ")

# #Exercicio 1 
# # Tente criar um código que conte de 1 a 10 mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5. )

# for conta in range(1,11):
#     if conta != 5:
#     print(f"Sensor n°{sensor}com falha")
#     print(f"Nenhuma falha no sensor!")
#     continue
# print("Fim! :)")

#  # Exercicio 2
#  #  Simule um semaforo com parada para cada cor. Determine um tempo para que quando mudar para tal cor ele represente uma pausa para cada cor. Use o continue para pular a cor amarelo (simulando um semáforo com defeito que não acende a luz amarela).
# # import time 
# # cor = ["verde", "amarelo", "vermelho"]
# # for semáforo in cor:
# #     if semáforo == "amarelo": 
# #         print(f"cor {semáforo} com falha!")
# #         continue
# #     print(f"cor {semáforo} acendida!")
# #     time.sleep(3)
# # print("Fim!")


# Exercicio 3 - Soma de Cargas de Energia (for)
# Uma fabrica tem 5 máquinas. Peças ao usuarios (via input dentro do loop) o consumo em kwh de cada uma das 5 maquinas. Ao final do loop. O programa deve exibir o consumo total de fábrica.
# total_consumo = 0
# for maquina in range(1, 6):
#     consumo = float(input(f"Digite o consumo em kwh da máquina {maquia}"))
#     total_consumo += #Acumulo 
print("O consumo total de fabrica é de {total_consumo}KwH.")

