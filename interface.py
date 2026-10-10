from tarefas import cadastrar, listar, atualizar, remover, repetir_tarefa, validar_data
from persistencia import salvar_tarefas, carregar_tarefas
#Arriba estoy importando las tareas y la persistencia

def escolher_opcao(mensagem, opcoes):
    # Muestro as opcoes e volto a perguntar se digitar errado.
    while True:
        print(mensagem)
        for numero, opcao in enumerate(opcoes, 1):
            print(numero, '-', opcao)
        escolha = input('Escolha: ')
        if escolha.isdigit():
            numero = int(escolha)
            if numero >= 1 and numero <= len(opcoes):
                return opcoes[numero - 1]
        print('Opcao invalida, tenta de novo!')


def pedir_data(obrigatoria=True):
    while True:
        data = input('Data de vencimento (dd/mm/aaaa): ')
        if data == '' and not obrigatoria:
            return ''
        if validar_data(data):
            return data
        print('Data invalida. Exemplo: 25/10/2026')


def escolher_tarefa(tarefas):
    if len(tarefas) == 0:
        print('Ainda nao tem tarefas.')
        return 0
    listar(tarefas)
    numero = input('Numero da tarefa: ')
    if numero.isdigit():
        numero = int(numero)
        if numero >= 1 and numero <= len(tarefas):
            return numero
    print('Numero invalido!')
    return 0


def executar():
    tarefas = carregar_tarefas()
    print('Bem-vindo ao Gerenciador de Tarefas!')
    while True:
        print('\n========== MENU ==========')
        print('1 - Cadastrar tarefa')
        print('2 - Listar tarefas')
        print('3 - Filtrar tarefas')
        print('4 - Atualizar tarefa')
        print('5 - Remover tarefa')
        print('6 - Repetir tarefa semanal')
        print('0 - Sair')
        opcao = input('Digite sua opcao: ')

        if opcao == '1':
            descricao = input('Descricao: ')
            if descricao == '' or ';' in descricao or '\n' in descricao:
                print('Descricao nao pode estar vazia nem ter ponto e virgula.')
                continue
            data = pedir_data()
            prioridade = escolher_opcao('Prioridade:', ['baixa', 'media', 'alta'])
            categoria = escolher_opcao('Categoria:', ['trabalho', 'pessoal', 'estudos'])
            repeticao = escolher_opcao('Repeticao:', ['nenhuma', 'semanal'])
            cadastrar(tarefas, descricao, data, prioridade, categoria, repeticao)
            # Salvo depois de cada mudanca, por si fechar o programa.
            salvar_tarefas(tarefas)
            print('Tarefa cadastrada!')

        elif opcao == '2':
            listar(tarefas)

        elif opcao == '3':
            filtro = escolher_opcao('Filtrar por:', ['status', 'data'])
            if filtro == 'status':
                status = escolher_opcao('Status:', ['pendente', 'em andamento', 'concluida'])
                listar(tarefas, filtro_status=status)
            else:
                data = pedir_data()
                listar(tarefas, filtro_data=data)

        elif opcao == '4':
            numero = escolher_tarefa(tarefas)
            if numero != 0:
                print('Deixa vazio se nao quiser mudar.')
                descricao = input('Nova descricao: ')
                if ';' in descricao or '\n' in descricao:
                    print('Nao pode usar ponto e virgula.')
                    continue
                data = pedir_data(False)
                mudar = input('Quer mudar o status? (s/n): ')
                status = ''
                if mudar == 's':
                    status = escolher_opcao('Novo status:', ['pendente', 'em andamento', 'concluida'])
                atualizar(tarefas, numero, descricao, data, status)
                salvar_tarefas(tarefas)
                print('Tarefa atualizada!')

        elif opcao == '5':
            numero = escolher_tarefa(tarefas)
            if numero != 0:
                confirmar = input('Confirma remover? (s/n): ')
                if confirmar == 's':
                    remover(tarefas, numero)
                    salvar_tarefas(tarefas)
                    print('Tarefa removida!')

        elif opcao == '6':
            numero = escolher_tarefa(tarefas)
            if numero != 0:
                if tarefas[numero - 1][5] == 'semanal':
                    print('Coloca a data da proxima semana:')
                    nova_data = pedir_data()
                    repetir_tarefa(tarefas, numero, nova_data)
                    salvar_tarefas(tarefas)
                    print('Nova tarefa semanal cadastrada!')
                else:
                    print('Essa tarefa nao e semanal.')

        elif opcao == '0':
            salvar_tarefas(tarefas)
            print('Ate a proxima!')
            break
        else:
            print('Opcao invalida!')
