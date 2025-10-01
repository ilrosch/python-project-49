import prompt

from .cli import welcome_user

COUNT_ROUNDS = 3


def launch_game(rules, def_game):
    user_name = welcome_user()
    print(rules)
    
    for _ in range(COUNT_ROUNDS):
        question, answer = def_game()
        
        print('Question:', question)
        user_answer = prompt.string('Your answer: ').lower()
        
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. \
              Correct answer was '{answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        
        print('Correct!')

    print('Congratulations,', user_name)  