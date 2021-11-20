from acme.selection import get_input

from . import message


def play():
    print('First Character Main Play')

    message.start()
    first_phase()


def first_phase():

    desired_answer = 's'

    condition = True
    while condition:

        message.first_phase()
        answer = get_input()

        if answer not in ['s', 'n']:
            message.error()
            continue

        if answer == desired_answer:
            second_phase()
            condition = False

        else:
            message.game_over()
            condition = False


def second_phase():

    desired_answer = 's'

    condition = True
    while condition:

        message.second_phase()
        answer = get_input()

        if answer not in ['s', 'n']:
            message.error()
            continue

        if answer == desired_answer:
            third_phase()
            condition = False

        else:
            message.game_over()
            condition = False

def third_phase():

    desired_answer = 's'

    condition = True
    while condition:

        message.third_phase()
        answer = get_input()

        if answer not in ['s', 'n']:
            message.error()
            continue

        if answer == desired_answer:
            message.game_win()
            condition = False

        else:
            message.game_over()
            condition = False