# Cada tarefa e uma lista: descricao, data, status, prioridade, categoria e repeticao.

def validar_data(data):
    # Confiro o formato da data sem usar biblioteca extra.
    partes = data.split('/')
    if len(partes) != 3:
        return False
    dia = partes[0]
    mes = partes[1]
    ano = partes[2]
    if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
        return False
    if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
        return False
    if int(dia) < 1 or int(dia) > 31 or int(mes) < 1 or int(mes) > 12:
        return False
    return True


def cadastrar(tarefas, descricao, data, prioridade, categoria, repeticao):
    # Toda tarefa nova comeca como pendente.
    tarefas.append([descricao, data, 'pendente', prioridade, categoria, repeticao])


def listar(tarefas, filtro_status='', filtro_data=''):
    encontrou = False
    for numero, tarefa in enumerate(tarefas, 1):
        if (filtro_status == '' or tarefa[2] == filtro_status) and (filtro_data == '' or tarefa[1] == filtro_data):
            encontrou = True
            print('\nTarefa', numero)
            print('Descricao:', tarefa[0])
            print('Vencimento:', tarefa[1])
            print('Status:', tarefa[2])
            print('Prioridade:', tarefa[3])
            print('Categoria:', tarefa[4])
            print('Repeticao:', tarefa[5])
    if not encontrou:
        print('Nenhuma tarefa encontrada.')


def atualizar(tarefas, numero, descricao, data, status):
    # Se deixar vazio, mantenho o valor que ja estava.
    tarefa = tarefas[numero - 1]
    if descricao != '':
        tarefa[0] = descricao
    if data != '':
        tarefa[1] = data
    if status != '':
        tarefa[2] = status


def remover(tarefas, numero):
    tarefas.pop(numero - 1)


def repetir_tarefa(tarefas, numero, nova_data):
    # Para as semanais, duplico manualmente e coloco a proxima data.
    tarefa = tarefas[numero - 1]
    tarefas.append([tarefa[0], nova_data, 'pendente', tarefa[3], tarefa[4], tarefa[5]])
