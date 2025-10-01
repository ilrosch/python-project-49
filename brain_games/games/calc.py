from ..launch_game import launch_game
from ..random import get_random_number


def calc(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b


def generate_question_parity():
    number_a = get_random_number(100)
    number_b = get_random_number(100)
    
    operations = ['*', '+', '-']
    operation = operations[get_random_number(2)]
    
    question = f"{number_a} {operation} {number_b}"
    correct_answer = str(calc(number_a, number_b, operation))
    
    return (question, correct_answer)
    

rules = 'What is the result of the expression?'


def start_calc_game():
    return launch_game(rules, generate_question_parity)