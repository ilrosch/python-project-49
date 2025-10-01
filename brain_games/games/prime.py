from math import floor, sqrt

from ..launch_game import launch_game
from ..random import get_random_number


def is_prime(num):
    for n in range(2, floor(sqrt(num))):
        if num % n == 0:
            return False

    return True


def generate_question_parity():
    number = get_random_number(100, 1)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return (number, correct_answer)
  

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_game():
    return launch_game(rules, generate_question_parity)