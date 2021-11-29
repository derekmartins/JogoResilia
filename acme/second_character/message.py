def error():
    print("Você digitou errado, por favor escolha uma opção válida")


def start():
    print('''
    Você é Paulo Bolk, Chefe de Produção, que está querendo uma promoção.
    ''')


def first_phase():
    print('''

    Imagina uma mega história aqui...
    - Máquina sem Manutenção a 3 meses

    1 - Você ignora o problema da máquina, pois deseja muito a promoção.
    2 - Você faz o pedido de uma máquina nova.
    ''')


def second_phase():
    print('''

    - Parabéns, você avançou
    - Você entrega o trabalho a tempo
    - Um tempo depois os problemas chegam
    - A máquina superaquece
    - Escutasse um barulho
    - A máquina solta uma peça
    - A máquina deu problema
    - Você descobre que um  dos seus funcionários deixou uma pulseira cair na máquina.

    1 - Orienta o funcionário, a seguir as normas de segurança.
    2 - Você demite a pessoa, afinal foi falta de atenção dela.
    '''.replace('    ', ''))


def third_phase():
    print('''

    O colega não reage bem as normas de Segurança do Trabalho.
    E o funcionário te agride.

    1 - Você revida com a primeira vassoura que você viu perto.
    2 - Chama o segurança, para conter a situação.
    '''.replace('    ', ''))


def first_phase_game_over():
    print('''

    VOCÊ PERDEU!!!

    Seus superiores não curtiram a ideia de comprar uma máquina nova.
    Pois assim você estourou o orçamento da empresa.
    
    '''.replace('    ', ''))


def second_phase_game_over():
    print('''

    '''.replace('    ', ''))


def third_phase_game_over():
    print('''

    Você perdeu o seu emprego, por mau comportamento.
    Tadinha da vassoura, ela não tinha nada a ver com a história.

    '''.replace('    ', ''))


def game_win():
    print('''
    Parabéns, o Segurança Carlão usou a primeira vassoura que viu pela frente
    e bateu no funcionário.

    A empresa está orgulhosa de você, pois você aumentou a produtividade
    e segurança dos funcionários.
    
    Porém você foi chamado para uma conversa com o RH, sobre suas soft skills, 
    mas isso é história para outro jogo...
    
    Fim...
    ''')
