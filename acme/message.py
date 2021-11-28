def start():
    print(
        '''
    Seja bem vindo à Empresa Makina Poincaré.
    Você está com as contas atrasadas e apareceu algumas oportunidades
    de emprego, você deve escolher uma das profissões abaixo.
    '''.replace("    ", ''))


def menu():
    print('''
    1. Arthur, um jovem publicitário em uma vaga de estágio.
    '''.replace("    ", ''))


def error():
    print("Você digitou errado, por favor escolha uma opção válida")


def first_character_start():
    pass


def play_again():
    print('''
    Você deseja jogar novamente?
    
    S - Sim
    N - Não
    '''.replace('    ',''))


def play_again_success():
    print('Parabéns, vamos jogar de novo')


def bye():
    print("Adeus, obrigado por ter jogado!")
