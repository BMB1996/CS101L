import math

def menu():
    print('{:^25s}'.format('Grade Menu'))
    print('1 -Add Test')
    print('2 -Remove Test')
    print('3 -Clear Tests')
    print('4 -Add Assignment')
    print('5 -Remove Assignment')
    print('6 -Clear Assignment')
    print('D -Display Scores')
    print('Q -Quit')

def add_grade(grade, menu_option):
    try:
        if int(grade) < 0:
            print('Invalid score.')
        else:
            if menu_option == '1':
                lst_test.append(int(grade))
            else:
                lst_assignment.append(int(grade))
    except ValueError:
        print('Must be a number.')

def remove_grade(grade, menu_option):
    try:
        if int(grade) < 0:
            print('Invalid score.')
        else:
            if menu_option == '2':
                if int(grade) in lst_test:
                    lst_test.remove(int(grade))
                else:
                    print('Grade not found in tests')
            else:
                if int(grade) in lst_assignment:
                    lst_assignment.remove(int(grade))
                else:
                    print('Grade not found in assignments')
    except ValueError:
        print('Must be a number.')

def mean(lst):
    try:
        avg = sum(lst)/len(lst)
    except ZeroDivisionError:
        return 0
    return avg

def sd(lst):
    avg = mean(lst)
    numerator = 0
    try:
        for i in range (0,len(lst)):
            x = (lst[i] - avg) ** 2
            numerator += x
        inside = numerator / len(lst)
        stand_dev = math.sqrt(inside)
    except ZeroDivisionError:
        return 0
    return stand_dev

lst_test = []
lst_assignment = []

start = True
while start == True:
    menu()
    get_input = input('\nSelect a menu option: ')
    if get_input == '1':
        add_grade(input('\nEnter the new grade: '), get_input)
    elif get_input == '2':
        remove_grade(input('\nEnter the grade to remove: '), get_input)
    elif get_input == '3':
        lst_test.clear()
    elif get_input == '4':
        add_grade(input('\nEnter the new grade: '), get_input)
    elif get_input == '5':
        remove_grade(input('\nEnter the grade to remove: '), get_input)
    elif get_input == '6':
        lst_assignment.clear()
    elif get_input.lower() == 'd':
        print('{:<13}{:>2}{:>7}{:>7}{:>7}{:>7}'.format('Type','#','Min','Max','Avg','StDev'))
        print('=' * 43)
        if len(lst_test) >= 1:
            print('{:<13}{:>2}{:>7.2f}{:>7.2f}{:>7.2f}{:>7.2f}'.format('Tests', len(lst_test), min(lst_test), max(lst_test),mean(lst_test),sd(lst_test)))
        else:
            print('{:<13}{:>2}{:>7}{:>7}{:>7}{:>7}'.format('Tests', '0', 'N/A', 'N/A', 'N/A', 'N/A'))
        if len(lst_assignment) >= 1:
            print('{:<13}{:>2}{:>7.2f}{:>7.2f}{:>7.2f}{:>7.2f}'.format('Assignments', len(lst_assignment), min(lst_assignment), max(lst_assignment),mean(lst_assignment),sd(lst_assignment)))
        else:
            print('{:<13}{:>2}{:>7}{:>7}{:>7}{:>7}'.format('Tests', '0', 'N/A', 'N/A', 'N/A', 'N/A'))
        print('The weighted score is: ', (mean(lst_test)*0.6) + (mean(lst_assignment)*0.4))
    elif get_input.lower() == 'q':
        start = False
