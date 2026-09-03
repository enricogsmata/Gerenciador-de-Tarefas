# main.py
import os
from . import task

# Imprime as opções do menu
def imprimir_menu():
    print("=== MENU ===")
    print("[1] Adicionar Tarefa")
    print("[2] Listar Tarefas")
    print("[3] Concluir Tarefa")
    print("[4] Remover Tarefa")
    print("[5] Sair")
    
# Valida a opção (int) selecionada pelo usuário. Previne opções incorretas
def validar_opcao(opcao: int) -> bool:
    if not isinstance(opcao, int) or (opcao < 1 or opcao > 5 ):
        return False
    
    return True

def executar_opcao(opcao: int) -> bool:
    # A partir da opção selecionada, delega para a função específica
    match opcao:
        case 1:
            task.adicionar_tarefa()
        case 2:
            task.listar_tarefas()
        case 3:
            task.concluir_tarefa()
        case 4:
            task.remover_tarefa()
        case _:
            return False
        
    return True

def main():
    opcao = 0
    
    while opcao != 5:
        # 1. Imprime as opções disponíveis do menu
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_menu()
        
        # 2. Solicita a opção para o usuário
        try: 
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("Valor inserido é inválido! Deve ser inserido um valor numérico.")
            continue
        
        # 3. Valida a opção digitada pelo usuário
        if not validar_opcao(opcao):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida!")
            continue
    
        # 4. Se a opção for válida, delega para a ação selecionada
        if opcao == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saindo do sistema...")
            break
        
        # Se o usuário digitou uma opção inválida, exibe erro
        if not executar_opcao(opcao):
            print("Opção inválida!")
            input("Pressione qualquer tecla para prosseguir...")
            continue
    
if __name__ == "__main__":
    main()