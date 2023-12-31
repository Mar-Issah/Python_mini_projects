import random

rand_number = random.randint(0, 5)
guesses = 0

while True:
    guesses += 1
    number = input('Guess the number: ')

    if number.isdigit():
        number = int(number)

        if number <= 0:
            print('Please guess a number greater than zero')
            continue
    else:
        print('Please guess only numbers')
        continue

    if number == rand_number:
        print('Correct!')
        break
    elif number > rand_number:
        print('Your guess was higher than the number')
    else:
        print('Your guess was below than the number')

print(f'You got it right in {guesses} guesses')