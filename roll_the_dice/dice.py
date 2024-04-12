import random

while True:
    print('Welcome to the dice rolling simulator!')
    input_dice = input('Press enter to roll the dice or type "exit" to quit.')
    if input_dice == 'exit':
        break
    else:
        print(random.randint(1, 6))