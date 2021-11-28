def menu():
    print("Imagina um mega menu aqui...")


def error():
    print("Você digitou errado, por favor escolha uma opção válida")


def start():
    print('''
    Você escolheu o ser Arthur, o Publicitário da Empresa MakinaPoincaré.
    Você é de suma importância para a empresa, portanto você passa
    o dia todo subindo e descendo andares, resolvendo problemas.
    '''.replace('    ', ''))


def first_phase():
    print('''
    Você está carregando uma carga de 152kg para entregar ao seu chefe, e precisa usar o elevador, 
    mas o elevador só suporta 150kg. O que você faz?
    
    1 - Você tenta subir de elevador com tudo de uma vez, pois tempo é dinheiro!
    2 - Você sobe as escadas, pois acha que é mais seguro, pois segurança em primeiro lugar!
    '''.replace('    ', ''))


def second_phase():
    print('''
    Parabéns! Você avançou para a Segunda Fase xD.
    
    Infelizmente te avisamos, que era uma situação perigosa.
    Você agora está no hospital e acabou de acordar.

    Ao tomar consciência você percebe que recebeu uma visita inesperada: 
    Ivo Asimov, o seu Chefe. 
    
    Você fica alegre pelo reconhecimento, mas logo logo fica desconfiado.
    Seu chefe começa algumas conversas estranhas e no final faz a 
    seguinte proposta:

    Oferece a você um valor de 250.000 reais, para não colocar a empresa 
    na justiça e não comentar nada sobre o caso. O que você faz?

    1 - Você aceita a propina de 250.000, pois dinheiro não nasce em árvore.
    2 - Você rejeita a propina de 250.000, pois quer manter a consciência limpa. 
    '''.replace('    ', ''))


def third_phase():
    print('''
    Você avançou para a Terceira Fase.
    Dava pra sentir de longe, o cheiro de falcatrua e isso se confirmou.
    Seu chefe está sendo investigado por sonegação de imposto
    e desvio de recursos da empresa.

    Ainda bem que você é uma pessoa honesta e não se submete, quando
    é colocado nessas condições.

    Graças ao seu bom comportamento, o dono da MakinaPoincaré, Gary Mag Carl,
    conversar sobre o seu futuro e lhe fazer um pedido.
    Não entrar na justiça, para que isso não seja noticiado na imprensa
    local. Você é publicitário, você sabe que isso pode queimar a
    imagem criada pela empresa. Em troca, você ganhar uma quantia simbólica
    para o seu tratamento e para pagar as suas contas básicas.
    
    O que você faz?

    1 - Você não aceita a proposta e entra na justiça, pois quer ganhar honestamente.
    2 - Você aceita a proposta do seu chefe, afinal ele está sendo seu amigo.
    '''.replace('    ', ''))


def first_phase_game_over(answer):
    print('''
    VOCÊ PERDEU!!!

    Você demorou demais para entregar a documentação e os itens que o seu chefe pediu, 
    por conta disso, você foi demitido por "justa causa"
    '''.replace('    ', ''))


def second_phase_game_over(answer):
    print('''
    VOCÊ PERDEU!!!
    
    Seu chefe estava sendo investigado por sonegação de impostos e
    desvio de verba da empresa. Iso Asimov foi preso. Você também
    foi preso por aceitar a propina.
    '''.replace('    ', ''))


def third_phase_game_over(answer):
    print('''
    VOCÊ PERDEU!!!
    
    A proposta do seu chefe, era uma tentativa de economizar recursos.
    O que você recebia uma quantia em dinheiro que estava muito abaixo 
    do que era suficiente para você custear suas despesas. Por conta 
    disso você foi despejado e virou morador de rua.
    '''.replace('    ', ''))



def game_win():
    print('''
    PARABÉNS

    Você entrou na justiça e ganhou o processo.
    Realmente o dono da empresa estava agindo de má fé e tinha receio
    de que isso o prejudicasse no negócio.
    
    Depois de muita luta, você vai ser indenizado pela empresa, com o valor
    de 350 mil reais, para arcar com todas as suas despesas durante o período
    de recuperação. 

    '''.replace('    ', ''))