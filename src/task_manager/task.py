# task.py
import os
from . import data

# Adiciona uma nova tarefa à lista de tarefas
def adicionar_tarefa() -> None:
    # Solicita ao usuário o nome da tarefa a ser inserida
    os.system('cls' if os.name == 'nt' else 'clear')
    nome_tarefa = None
    
    while not nome_tarefa:
        nome_tarefa = input("Digite o nome da tarefa: ")
        
    # Quando o nome inserido não for nulo ou vazio, insere a nova tarefa na lista de tarefas
    nova_tarefa = {"nome": nome_tarefa, "status": "Pendente"}
    data.tarefas.append(nova_tarefa)
    
    print("Tarefa adicionada com sucesso!")
    input("Pressione qualquer tecla para prosseguir...")
    
# Lista tarefas disponiveis na lista de tarefas
def listar_tarefas() -> None:
    # Imprime cada elemento formatado
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if len(data.tarefas) == 0:
        print("Nenhuma tarefa adicionada!")
    else:
        for tarefa in data.tarefas:
            if (tarefa.get("nome")):
                print(f"{tarefa["nome"]}: {tarefa["status"]}")
    
    input("Pressione qualquer tecla para prosseguir...")
    
# Define o status de uma tarefa como Concluído
def concluir_tarefa() -> None:
    # Solicita o nome da tarefa que o usuário deseja concluir
    os.system('cls' if os.name == 'nt' else 'clear')
    nome_tarefa = None
    
    while not nome_tarefa:
        nome_tarefa = input("Digite o nome da tarefa: ")
    
    # Verifica se a tarefa consta na lista de tarefas
    # 1. Se sim, altera o status para Concluido
    # 2. Se não, exibe mensagem e sai do processo
    tarefa_encontrada = False
    
    for tarefa in data.tarefas:
        if tarefa.get("nome") == nome_tarefa:
            tarefa["status"] = "Concluido"
            tarefa_encontrada = True
    
    if not tarefa_encontrada:
        print("Tarefa não encontrada! Nenhuma alteração foi realizada.")
    else:
        print("Status atualizado com sucesso!")
        
    input("Pressione qualquer tecla para prosseguir...")
        
# Remove uma tarefa da lista de tarefas
def remover_tarefa() -> None:
    # Solicita o nome da tarefa que o usuário deseja concluir
    os.system('cls' if os.name == 'nt' else 'clear')
    nome_tarefa = None
    
    while (not nome_tarefa):
        nome_tarefa = input("Digite o nome da tarefa: ")
    
    # Remove todos os objetos que não contenham o nome da tarefa informado
    if not any(tarefa for tarefa in data.tarefas if tarefa.get("nome") == nome_tarefa):
        print("Tarefa não encontrada! Nenhuma alteração foi realizada.")
    else:
        data.tarefas = [tarefa for tarefa in data.tarefas if (tarefa.get("nome") != nome_tarefa)]
    
    input("Pressione qualquer tecla para prosseguir...")