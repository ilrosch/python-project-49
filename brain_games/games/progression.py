from ..launch_game import launch_game
from ..random import get_random_number


def get_progression(start, length, diff): 
    def next_element(index):
        return start + index * diff
    
    return [str(next_element(i)) for i in range(length)]


def generate_question_parity():
    number = get_random_number(50)
    length = get_random_number(10, 5)
    skip = get_random_number(length - 1)
    diff = get_random_number(50, -50)
    
    progression = get_progression(number, length, diff)
    correct_answer = str(progression[skip])
    progression[skip] = '..'
    question = ' '.join(progression)

    return (question, correct_answer)
  

rules = 'What number is missing in the progression?'


def start_game():
    return launch_game(rules, generate_question_parity)
