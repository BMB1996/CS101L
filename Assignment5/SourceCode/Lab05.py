########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


import string


def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return (ord(char) - 65)
    elif ord(char) >= ord('0') and ord(char) <= ord('9'):
        return ord(char) - ord('0')
    else:
        return -1

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    #Might be a problem
    T_or_F, valid = is_valid(idnumber)
    if T_or_F == True:
        index = 1
        total = 0
        for i in idnumber[:-1]:
            if character_value(i) == -1:
                break
            temp = index * character_value(i)
            total += temp
            index += 1
        else:
            check_digit = total % 10
            return check_digit
    else:
        return -1

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    for i in idnumber[:5]:
        if ord(i.upper()) <= ord('Z') and ord(i.upper()) >= ord('A'):
            valid = True
        else:
            valid = False
            break
    if valid == True:
        if get_school(idnumber) != -1:
            if get_grade(idnumber) != -1:
                if idnumber[7:9].isdigit() == True:
                    return True, ''
                else:
                    return False, 'Characters 8 and 9 must be digits'
            else:
                return False, 'Character 7 must be 1-4'
        else:
            return False, 'Character 6 must be 1-3'
    return False, 'The first 5 characters must be letters'

def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    verify, error = is_valid(idnumber)
    check = get_check_digit(idnumber)
    if verify == False:
        return False, error
    if get_check_digit(idnumber) == int(idnumber[-1]):
        return True, -1
    else:
        return False, 'Check digit {} doesn\'t match calculated value of {}'.format(idnumber[-1], check)

def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if ord(idnumber[5]) == ord('1'):
        return 'School of Computing and Engineering SCE'
    elif ord(idnumber[5]) == ord('2'):
        return 'School of Law'
    elif ord(idnumber[5]) == ord('3'):
        return 'College of Arts and Sciences'
    else:
        return -1

def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    if ord(idnumber[6]) == ord('1'):
       return 'Freshman'
    elif ord(idnumber[6]) == ord('2'):
       return 'Sophomore'
    elif ord(idnumber[6]) == ord('3'):
       return 'Junior'
    elif ord(idnumber[6]) == ord('4'):
       return 'Senior'
    else:
        return -1

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        