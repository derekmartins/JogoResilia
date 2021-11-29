def error():
    print("Você digitou errado, por favor escolha uma opção válida")


def start():
    print('''
    Você trabalha como zelador noturno do prédio de uma grande corporação, 
    uma multinacional super-conhecida, e vai ficar trabalhando durante o 
    final de semana, para tomar conta do prédio e realizar uma limpeza geral. 
    Na sexta feira por volta das 18h, o pessoal começa a sair de seus escritórios, 
    você nota que aquele momento pra eles será de total descanso, um happy-hour. 
    O tempo passa, e por volta das 19:30, você está limpando o corredor principal do 
    4º andar do prédio, e verifica que alguém vestido com um terno executivo sai de 
    uma das salas, com um notebook nas mãos, qual a sua atitude ?    
    ''')


def first_phase():
    print('''

    ### Pergunta

    1 - Perguntava a ele o que estava fazendo ali.
    2 - Apenas finge que aquilo não está acontecendo, porém grava tudo com seu celular para registro.
    ''')


def second_phase():
    print('''
    Você fez vista grossa... ao menos finge que fez, pois com seu celular você grava a ação do executivo.

    Após ter o vídeo em mãos, você tem provas de um suposto caso de roubo dentro do ambiente de trabalho, 
    e precisa decidir o que seria moralmente correto nessa situação.
    Qual sua atitude ?

    1 - Você opta por levar o vídeo até o seu chefe, com intuito de informar sobre a má conduta do executivo.
    2 - Decide levar o vídeo ao órgão público responsável por regulamentar a segurança do trabalho.

    '''.replace('    ', ''))


def third_phase():
    print('''

    Seu vídeo serve como prova contra o alto executivo, que recebe uma notificação de demissão.
    Após a demissão por justa causa do advogado, o mesmo entra em contato com você via telefone, 
    ameaçando você e a sua família pelo que fizeram a ele,  o que você faz ?

    1 - Tenta conversar com ele e explicar a situação, sobre como o que ele fez é errado e traz prejuízos a empresa e a moral.
    2 - Vai até a polícia e registra um B.O. contra o agora ex-executivo, uma vez que ele está fazendo ameaças a sua pessoa.
   
    '''.replace('    ', ''))


def first_phase_game_over():
    print('''
    VOCÊ PERDEU!!!

    Ele diz não ser da sua conta, e te manda voltar ao trabalho grosseiramente. 
    Você fica sem ação, e acaba fazendo vista grossa para um possível furto.

    
    '''.replace('    ', ''))


def second_phase_game_over():
    print('''

    VOCÊ PERDEU!!!

    Apesar da atitude ser a correta, seu chefe te informa que infelizmente não poderá fazer nada, 
    pois senão ele também seria demitido, e não quis se envolver.
    '''.replace('    ', ''))


def third_phase_game_over():
    print('''
    O executivo não quer saber sobre, ele está tomado pela fúria e tudo que quer saber é de vingança. 
    Seria mais prudente ter ido a polícia relatar o ocorrido.   
    '''.replace('    ', ''))


def game_win():
    print('''

    PARABÉNS

    Agindo conforme manda a lei, você garante a sua proteção e de seus parentes também, 
    o agora ex-executivo é preso e sentenciado a serviço comunitário.

    Agora você volta a trabalhar tranquilamente.

    ''')
