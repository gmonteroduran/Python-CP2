# Salvo tudo num txt
ARQUIVO = 'tarefas.txt'


def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for tarefa in tarefas:
            # O ponto e virgula separa cada informacao da tarefa.
            arquivo.write(';'.join(tarefa) + '\n')


def carregar_tarefas():
    tarefas = []
    # O tarefas.txt ja vem no projeto. Nao precisa criar a mao.
    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            if len(dados) == 6:
                tarefas.append(dados)
    return tarefas
