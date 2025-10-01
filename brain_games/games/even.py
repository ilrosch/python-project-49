from ..launch_game import launch_game
from ..random import get_random_number


def isEven(num): 
    return num % 2 == 0


def generate_question_parity():
    number = get_random_number(100)
    correct_answer = 'yes' if isEven(number) else 'no'
    return (number, correct_answer)
  

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def startEvenGame():
    return launch_game(rules, generate_question_parity)
