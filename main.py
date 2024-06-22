import os
import demon_ui
import json
import random


def load_word():
    """ Loads the words for random generator """
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        list_words = [word.strip().lower() for word in data['word_list']['es']]
        play_word = list_words[random.randint(0, len(list_words)-1)]
        return play_word


def fail_attemp(lives):
    if lives == 5:
        return(demon_ui.load_demon_stage1('Let the game begins... ' + str(lives) + ' lives left!'))
    if lives == 4:
        return(demon_ui.load_demon_stage2('Oh oh, bad start... ' + str(lives) + ' lives left!'))
    if lives == 3:
        return(demon_ui.load_demon_stage3('Ouch, other try... ' + str(lives) + ' lives left!'))
    if lives == 2:
        return(demon_ui.load_demon_stage4('Ummm seems not good for you... just' + str(lives) + ' lives left!'))
    if lives == 1:
        return(demon_ui.load_demon_stage5('One more mistake... '))


def game(play_word, option, game_table):
    """ Sets the instance for a game run """
    if option in play_word:
        for i in range(len(game_table)):
            if option == play_word[i]:
                game_table[i] = option
        return game_table, True
    else:
        return game_table, False


if __name__ == '__main__':
    lives = 5

    play_word = load_word()

    game_table = ['_' for i in range(0, len(play_word))]

    os.system('clear')
    print(demon_ui.load_demon(
        " Let´s play a game if you lose, your soul will be mine."))
    option = input("Do you wanna play? (Y) (N) ... ")

    if option.upper() == "Y":
        os.system('clear')
        while True:
            print(fail_attemp(lives))
            print(''.join(game_table))
            option = input("Enter a word... ")
            if len(option) > 1:
                raise ValueError('Only one letter, silly...')
            else:
                os.system('clear')
                game_table, res = game(play_word, option, game_table)
                if res == False:
                    lives -= 1
                if game_table.count('_') > 0:
                    if lives == 0:
                        print(demon_ui.load_demon_wins(
                            'Now your soul its mine hahahaha...'))
                        break
                else:
                    os.system('clear')
                    print(demon_ui.load_demon("You Win!"))
                    break
    elif option.upper() == "N":
        os.system('clear')
        print(demon_ui.load_demon("Yeah sure, run! This is for the bravest only!"))
    else:
        os.system('clear')
        print(demon_ui.load_demon(
            "Please, follow the instructions or you will stay forever!"))
