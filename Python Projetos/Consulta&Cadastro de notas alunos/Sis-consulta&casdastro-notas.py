import tkinter as tk
from tkinter import ttk

# Dicionário para armazenar as informações dos alunos
alunos = {}

# Função para calcular a média das notas
def calcular_media(av1, av2):
    av1 = float(av1)
    av2 = float(av2)
    return (av1 + av2) / 2

# Função para cadastrar um aluno
def cadastrar_aluno():
    matricula = matricula_entry.get()
    nome = nome_entry.get()
    av1 = av1_entry.get()
    av2 = av2_entry.get()
    media = calcular_media(av1, av2)

    # Adicione o aluno ao dicionário
    alunos[matricula] = {
        'Nome': nome,
        'AV1': av1,
        'AV2': av2,
        'Média': media
    }

    # Limpe os campos de entrada
    matricula_entry.delete(0, tk.END)
    nome_entry.delete(0, tk.END)
    av1_entry.delete(0, tk.END)
    av2_entry.delete(0, tk.END)

    resultado_label.config(text=f"Aluno cadastrado:\nMatrícula: {matricula}\nNome: {nome}\nMédia: {media}")

# Função para consultar as notas de um aluno
def consultar_notas():
    matricula_consulta = matricula_consulta_entry.get()
    if matricula_consulta in alunos:
        aluno = alunos[matricula_consulta]
        resultado_consulta_label.config(text=f"Matrícula: {matricula_consulta}\nNome: {aluno['Nome']}\nAV1: {aluno['AV1']}\nAV2: {aluno['AV2']}\nMédia: {aluno['Média']}")
    else:
        resultado_consulta_label.config(text=f"Aluno com matrícula {matricula_consulta} não encontrado.")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Cadastro e Consulta de Notas")

# Rótulos e campos de entrada para o cadastro
matricula_label = ttk.Label(root, text="Matrícula:")
matricula_entry = ttk.Entry(root)
nome_label = ttk.Label(root, text="Nome:")
nome_entry = ttk.Entry(root)
av1_label = ttk.Label(root, text="AV1:")
av1_entry = ttk.Entry(root)
av2_label = ttk.Label(root, text="AV2:")
av2_entry = ttk.Entry(root)

# Botão para cadastrar o aluno
cadastrar_button = ttk.Button(root, text="Cadastrar", command=cadastrar_aluno)

# Rótulo para mostrar o resultado do cadastro
resultado_label = ttk.Label(root, text="")

# Rótulos e campos de entrada para a consulta
matricula_consulta_label = ttk.Label(root, text="Matrícula (para consulta):")
matricula_consulta_entry = ttk.Entry(root)

# Botão para consultar as notas do aluno
consultar_button = ttk.Button(root, text="Consultar Notas", command=consultar_notas)

# Rótulo para mostrar o resultado da consulta
resultado_consulta_label = ttk.Label(root, text="")

# Layout dos elementos na janela
matricula_label.grid(row=0, column=0)
matricula_entry.grid(row=0, column=1)
nome_label.grid(row=1, column=0)
nome_entry.grid(row=1, column=1)
av1_label.grid(row=2, column=0)
av1_entry.grid(row=2, column=1)
av2_label.grid(row=3, column=0)
av2_entry.grid(row=3, column=1)
cadastrar_button.grid(row=4, column=0, columnspan=2)
resultado_label.grid(row=5, column=0, columnspan=2)

matricula_consulta_label.grid(row=6, column=0)
matricula_consulta_entry.grid(row=6, column=1)
consultar_button.grid(row=7, column=0, columnspan=2)
resultado_consulta_label.grid(row=8, column=0, columnspan=2)

root.mainloop()