from os import system as sy
import time
sy('cls')

def gerenciador_tarefas():
    tarefas = []

    while True:
        print("\nGerenciador de Tarefas")
        print("1 - Adicionar Tarefa")
        print("2 - Marcar Tarefa como Concluída")
        print("3 - Remover Tarefa")
        print("4 - Listar Tarefas")
        print("5 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tarefa = input("Digite a tarefa: ")
            tarefas.append({"tarefa": tarefa, "concluída": False})
            print("Tarefa adicionada.")
        elif opcao == 2:
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas[indice]["concluída"] = True
                print("Tarefa marcada como concluída.")
            else:
                print("Índice inválido.")
        elif opcao == 3:
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(tarefas):
                tarefas.pop(indice)
                print("Tarefa removida.")
            else:
                print("Índice inválido.")
        elif opcao == 4:
            listar_tarefas(tarefas)
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa["concluída"] else "Pendente"
            print(f"{i}. {tarefa['tarefa']} - {status}")

gerenciador_tarefas()