# import tkinter as tk
# from tkinter import messagebox, ttk

# # # ATIVIDADE 1

# # .get() serve para buscar informação na caixa de texto
# def janela_bemvindo():
#     nome = nome_usuario.get()
#     turno = turno_usuario.get()
#     if nome == "" and turno -- "":
#         messagebox.showwarning("Aviso", "Digite seu nome :)")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Operador, {nome} registrado no turno {turno} - Seja bem-vindo ao nosso sistema")

#    # Janela 
# janela = tk.Tk()
# janela.title("Operador e Turno")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite seu nome :)")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_turno = tk.Label(janela, text="Digite seu turno :)")
# lbl_turno.grid(row=1, column=0, pady=10, padx=10)

# nome_usuario = tk.Entry(janela, font=("Arial", 12))
# nome_usuario.grid(row=0, column=1, pady=10, padx=10)

# turno_usuario = tk.Entry(janela, font=("Arial", 12))
# turno_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


# janela.mainloop()

# # ATIVIDADE 2

# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
   
#     numero1 = int(numero_usuario.get())
#     numero2 = int(pecas_usuario.get())
#     resultado = numero1 * numero2

#     if numero1 == "" and numero2 -- ""and resultado == "":
#         messagebox.showwarning("Digite a quantidade de peças: ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"A quantidade de peças é de: {resultado}")


#    # Janela 
# janela = tk.Tk()
# janela.title("Peças")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite a quantidade de peças:")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_horas = tk.Label(janela, text="Digite a quantidade de horas:")
# lbl_horas.grid(row=1, column=0, pady=10, padx=10)

# numero_usuario = tk.Entry(janela, font=("Arial", 12))
# numero_usuario.grid(row=0, column=1, pady=10, padx=10)

# pecas_usuario = tk.Entry(janela, font=("Arial", 12))
# pecas_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)


# janela.mainloop()


# # ATIVIDADE 3

# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
   
#     numero1 = float(bar_usuario.get())
#     numero2 = float(psi_usuario.get())
#     resultado = numero1 * numero2

#     if numero1 == "" and numero2 -- ""and resultado == "":
#         messagebox.showwarning("Digite a quantidade de peças: ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"A quantidade de peças é de: {resultado}")


#    # Janela 
# janela = tk.Tk()
# janela.title("Cauculo")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite a quantidade de Bar:")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# lbl_psi = tk.Label(janela, text="Digite o valor do PSI:")
# lbl_psi.grid(row=1, column=0, pady=10, padx=10)

# bar_usuario = tk.Entry(janela, font=("Arial", 12))
# bar_usuario.grid(row=0, column=1, pady=10, padx=10)

# psi_usuario = tk.Entry(janela, font=("Arial", 12))
# psi_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=0, pady=10, padx=10)

# janela.mainloop()

# # ATIVIDADE 4

# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
   
#     numero1 = float(media1_usuario.get())
#     numero2 = float(media2_usuario.get())
#     numero3 = int(media3_usuario.get())
#     resultado = (numero1) + (numero2) + (numero3) 
#     resultado /3

#     if numero1 == "" and numero2 -- ""and resultado == "":
#         messagebox.showwarning("Digite as 3 notas: ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"sua média é : {resultado}")


#    # Janela 
# janela = tk.Tk()
# janela.title("Cauculo")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_nota1= tk.Label(janela, text="Digite a primeira nota:")
# lbl_nota1.grid(row=0, column=0, pady=10, padx=10)

# lbl_nota2 = tk.Label(janela, text="Digite a segunda nota:")
# lbl_nota2.grid(row=1, column=0, pady=10, padx=10)

# lbl_nota3 = tk.Label(janela, text="Digite a terceira nota:")
# lbl_nota3.grid(row=2, column=0, pady=10, padx=10)

# media1_usuario = tk.Entry(janela, font=("Arial", 12))
# media1_usuario.grid(row=0, column=1, pady=10, padx=10)

# media2_usuario = tk.Entry(janela, font=("Arial", 12))
# media2_usuario.grid(row=1, column=1, pady=10, padx=10)

# media3_usuario = tk.Entry(janela, font=("Arial", 12))
# media3_usuario.grid(row=2, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
# btn_mensagem.grid(row=3, column=0, pady=10, padx=10)

# janela.mainloop()


# # ATIVIDADE 5

# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
   
#     numero1 = float(temperatura_usuario.get())


#     if numero1 < 40:
#         messagebox.showwarning("Bem-Vindo", "Está abaixo de 40°C: BAIXA CARGA")
#     elif numero1 > 40 and numero1 < 70:
#         messagebox.showwarning("Bem-Vindo", f"Está entre 40°C e 70°C: NORMAL")
#     elif numero1 > 70:
#         messagebox.showwarning("Bem-Vindo", f"Está acima de 70°C: ALERTA : Resfriamento ativado")
    
#     else:
#         messagebox.showinfo("Temperatura")


#    # Janela 
# janela = tk.Tk()
# janela.title("Cauculo")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite a temperatura do motor: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# temperatura_usuario = tk.Entry(janela, font=("Arial", 12))
# temperatura_usuario.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# janela.mainloop()


# ATIVIDADE 6

# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
   
#     letra = letra_usuario.get()


#     if letra == "a":
#         messagebox.showinfo("Bem-Vindo", "Código de Alimentos")
#     elif letra == "e":
#         messagebox.showinfo("Bem-Vindo", "Código de Eletrônico")
#     elif letra != "":
#         messagebox.showinfo("Bem-Vindo", "Código Desconhecido")
    
#     else:
#         messagebox.showinfo("Código")


#    # Janela 
# janela = tk.Tk()
# janela.title("Cauculo")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite a letra do código: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# letra_usuario = tk.Entry(janela, font=("Arial", 12))
# letra_usuario.grid(row=0, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Mensagem", command=janela_bemvindo)
# btn_mensagem.grid(row=1, column=0, pady=10, padx=10)

# janela.mainloop()


# ATIVIDADE 7

# import tkinter as tk
# from tkinter import messagebox, ttk

# def janela_bemvindo():
   
#     sensor = porta_usuario.get()
#     botao = botao_usuario.get()


#     if sensor == "fechada" and botao == "desligada":
#         messagebox.showinfo("Bem-Vindo", "Máquina Liberada para iniciar! ")
#     elif sensor == "aberta" and botao == "ligada":
#         messagebox.showinfo("Bem-Vindo", "Máquina não Liberada para iniciar! ")
#     elif sensor != "" and botao != "":
#         messagebox.showinfo("Bem-Vindo", "Erro ao passar o estado da máquina! ")
#     else:
#         messagebox.showerror("Erro", "Digite algo valido! ")


#    # Janela 
# janela = tk.Tk()
# janela.title("Máquina")
# janela.geometry("300x300")
# janela.configure(bg="pink")

#    # Componentes
# lbl_mensagem = tk.Label(janela, text="Digite o estado do sensor: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)
# lbl_mensagem = tk.Label(janela, text="Digite o estado do botao: ")
# lbl_mensagem.grid(row=1, column=0, pady=10, padx=10)

# porta_usuario = tk.Entry(janela, font=("Arial", 12))
# porta_usuario.grid(row=0, column=1, pady=10, padx=10)

# botao_usuario = tk.Entry(janela, font=("Arial", 12))
# botao_usuario.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
# btn_mensagem.grid(row=2, column=1, pady=10, padx=10)

# janela.mainloop()


# ATIVIDADE 8

import tkinter as tk
from tkinter import messagebox, ttk

def janela_bemvindo():
   
    numero1 = float(pecas_produzidas.get())
    numero2 = float(pecas_defeitos.get())
   
    
    if  numero1 > numero2 and numero2 > 5:
        messagebox.showwarning("Bem-Vindo", "Revisar processo!")
    elif numero1 > numero2:
        messagebox.showwarning("Bem-Vindo", "Processo Otimizado!")
   
    else:
        messagebox.showinfo("Tudo Certo!")


   # Janela 
janela = tk.Tk()
janela.title("Cauculo")
janela.geometry("500x200")
janela.configure(bg="pink")

   # Componentes
lbl_mensagem = tk.Label(janela, text="Digite a quantidade de pecas produzidas: ")
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

lbl_mensagem = tk.Label(janela, text="Digite a quantidade de pecas defeitos: ")
lbl_mensagem.grid(row=1, column=0, pady=10, padx=10)

pecas_produzidas= tk.Entry(janela, font=("Arial", 12))
pecas_produzidas.grid(row=0, column=1, pady=10, padx=10)

pecas_defeitos = tk.Entry(janela, font=("Arial", 12))
pecas_defeitos.grid(row=1, column=1, pady=10, padx=10)

btn_mensagem = tk.Button(janela, text="Confirmar", command=janela_bemvindo)
btn_mensagem.grid(row=2, column=1, pady=10, padx=10)

janela.mainloop()