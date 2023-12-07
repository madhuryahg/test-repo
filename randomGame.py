from random import randint
import sys


def generate_random_number(a, b):
    return randint(a, b)


first_num = int(sys.argv[1])
last_num = int(sys.argv[2])

rand_number = generate_random_number(first_num, last_num)

while True:
    try:
        user_num = int(input(f"Guess a number between {first_num} and {last_num}: "))
        if first_num < user_num <= last_num:
            if user_num == rand_number:
                print('You are a genius')
                break
            else:
                print('Ooops! Try again')
        else:
            print(f'Hey stupid. I said number between {first_num} anf {last_num} ')
    except ValueError as err:
        print(f'Please enter a number: {err}')
        continue
    finally:
        pass
