from acme import message, selection
from acme.first_character import main as first_character


def run():

    play_condition = True
    while play_condition:

        character_condition = True
        while character_condition:
            message.menu()
            response = selection.get_input()

            if response not in ['1', '2', '3']:
                message.error()

            if response == '1':
                first_character.play()
                character_condition = False


        play_again_condition = True
        while play_again_condition:

            message.play_again()
            answer = selection.get_input()

            if answer not in ['s', 'n']:
                message.error()
                continue

            if answer == 's':
                message.play_again_success()
                play_condition = True
                play_again_condition = False

            else:
                message.bye()
                play_condition = False
                play_again_condition = False
