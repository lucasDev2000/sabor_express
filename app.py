import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Sushi House', 'categoria':'Japonesa', 'ativo':False}]


def exibir_nome_programa():
    print('''
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        ''')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. SAIR\n')
    print()

def finalizar_app():
    exibir_subtitulo('Finalizando o programa')

def voltar_menu():
    print('Pressione uma tecla para voltar ao menu principal')
    input()
    main()

def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'| {texto} |')
    print(linha)
    print()


def cadastrar_novo_restaurante():
    '''
    Função para cadastrar um novo restaurante.

    Input:
    - nome: Nome do restaurante.
    - categoria: Categoria do restaurante.
    - ativo: Estado do restaurante (ativo ou inativo).

    Outputs:
    - Adiciona o restaurante à lista de restaurantes.

    '''

    exibir_subtitulo('Cadastrar novo restaurante')
    nome = input('Nome do restaurante: ')
    categoria = input(f'Categoria do restaurante {nome}: ')
    dados_do_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante "{nome}" cadastrado com sucesso!\n')
    voltar_menu()   

def listar_restaurantes():
    exibir_subtitulo('Listar restaurantes')


    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Ativo'.ljust(10)}')
    print('-' * 60)
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu() 

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante "{nome_restaurante}" foi ativado.' if restaurante['ativo'] else f'O restaurante "{nome_restaurante}" foi desativado.'
            print(mensagem)
            break
    if not restaurante_encontrado:
        print(f'O restaurante "{nome_restaurante}" não foi encontrado.')
    print('Pressione uma tecla para voltar ao menu principal')
    input()
    voltar_menu()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()  
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        print('Entrada inválida! Por favor, insira um número.')
        input('Pressione Enter para continuar...')
        main()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()