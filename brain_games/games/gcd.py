import math

from ..launch_game import launch_game
from ..random import get_random_number


def generate_question_parity():
    number_a = get_random_number(100, 1)
    number_b = get_random_number(100, 1)

    question = f"{number_a} {number_b}"
    correct_answer = str(math.gcd(number_a, number_b))
    
    return (question, correct_answer)
  

rules = 'Find the greatest common divisor of given numbers.'


def start_game():
    return launch_game(rules, generate_question_parity)