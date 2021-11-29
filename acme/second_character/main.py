from acme.selection import get_input

from . import message


def play():
    print('Second Character Main Play')

    message.start()
    first_phase()


def phase(start_message, answers, desired_answer, next_phase, game_over, has_input=True):

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
            game_over()
            condition = False


def first_phase():
    phase(message.first_phase, ['1', '2'], '1',
          second_phase, message.first_phase_game_over)


def second_phase():
    phase(message.second_phase, ['1', '2'], '1',
          third_phase, message.second_phase_game_over)


def third_phase():
    phase(message.third_phase, ['1', '2'], '2',
          message.game_win, message.third_phase_game_over)
