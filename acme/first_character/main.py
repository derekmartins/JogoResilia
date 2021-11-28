from acme.selection import get_input

from . import message


def play():
    message.start()
    first_phase()


def first_phase():

    desired_answer = '1'

    condition = True
    while condition:

        message.first_phase()
        answer = get_input()

        if answer not in ['1', '2']:
            message.error()
            continue

        if answer == desired_answer:
            second_phase()
            condition = False

        else:
            message.first_phase_game_over(answer)
            condition = False


def second_phase():

    desired_answer = '2'

    condition = True
    while condition:

        message.second_phase()
        answer = get_input()

        if answer not in ['1', '2']:
            message.error()
            continue

        if answer == desired_answer:
            third_phase()
            condition = False

        else:
            message.second_phase_game_over(answer)
            condition = False


def third_phase():

    desired_answer = '1'

    condition = True
    while condition:

        message.third_phase()
        answer = get_input()

        if answer not in ['1', '2']:
            message.error()
            continue

        if answer == desired_answer:
            message.game_win()
            condition = False

        else:
            message.third_phase_game_over(answer)
            condition = False
