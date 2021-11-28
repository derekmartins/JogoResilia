from acme.selection import get_input

from . import message


def play():
    print('Second Character Main Play')

    message.start()
    first_phase()

def phase(start_message, answers, desired_answer, next_phase, has_input = True):

    condition = True
    while condition:

        start_message()
        if has_input:
            answer = get_input()

        if answer not in answers:
            message.error()
            continue

        if answer == desired_answer:
            next_phase()
            condition = False

        else:
            message.game_over()
            condition = False    


def first_phase():
    phase(message.first_phase, ['1', '2', '3', '4'], '2', second_phase)


def second_phase():
    phase(message.second_phase, ['s', 'n'], 's', third_phase)

def third_phase():
    phase(message.third_phase, ['s', 'n'], 's', message.game_win)