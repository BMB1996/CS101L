
#CS 101 Lab
#Program 3
#Brandon Barber
#bmbct7@umsystem.edu

#Problem: Make a game to guess the users number based on the remainder when divided by 3, 5, and 7

play_again = 'Y'

print('Welcome to the Flarsheim Guesser!')
while play_again.lower() == 'y':
    print('Think of a number between and including 1 and 100.')
    mod_3 = int(input('What is the remainder when your number is divided by 3? '))
    while (mod_3 < 0) or (mod_3 > 2):
        if mod_3 < 0:
            print('The value entered must be 0 or greater.')
            mod_3 = int(input('What is the remainder when your number is divided by 3? '))
        else:
            print('The value entered must be less than 3.')
            mod_3 = int(input('What is the remainder when your number is divided by 3? '))
    mod_5 = int(input('What is the remainder when your number is divided by 5? '))
    while (mod_5 < 0) or (mod_5 > 4):
        if mod_5 < 0:
            print('The value entered must be 0 or greater.')
            mod_5 = int(input('What is the remainder when your number is divided by 5? '))
        else:
            print('The value entered must be less than 5.')
            mod_5 = int(input('What is the remainder when your number is divided by 5? '))
    mod_7 = int(input('What is the remainder when your number is divided by 7? '))
    while (mod_7 < 0) or (mod_7 > 6):
        if mod_7 < 0:
            print('The value entered must be 0 or greater.')
            mod_7 = int(input('What is the remainder when your number is divided by 7? '))
        else:
            print('The value entered must be less than 7.')
            mod_7 = int(input('What is the remainder when your number is divided by 7? '))
    mod_3_list = []
    mod_5_list = []
    mod_7_list = []
    for num in range (mod_3, 101, 3):
        mod_3_list.append(num)
    for num in range (mod_5, 101, 5):
        mod_5_list.append(num)
    for num in range (mod_7, 101, 7):
        mod_7_list.append(num)
    for number in mod_3_list:
        if number in mod_5_list and number in mod_7_list:
            print('Your number was {}'.format(number))
    play_again = input('Do you want to play again? Y to continue, N to quit ')
    while play_again != 'y'.lower() and play_again != 'n'.lower():
        play_again = input('Do you want to play again? Y to continue, N to quit ')

'''I am unsure if this would have been easier to write a function for the while if else loops in the mod_x sections.'''
