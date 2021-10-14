

def menu():
    print('MAIN MENU:\n\
1) Encode String\n\
2) Decode String\n\
Q) Quit')

def encrypt(text, shift):
    encrypted = ''
    for i in text.upper():
        if i.isalpha() == True:
            if (ord(i) + shift) > ord('Z'):
                encrypted += chr((ord(i) - 26) + shift)
            else:
                encrypted += chr(ord(i) + shift)
        else:
            encrypted += i
    return encrypted

def decrypt(text, shift):
    decrypted = ''
    for i in text.upper():
        if i.isalpha() == True:
            if (ord(i) - shift) < ord('A'):
                decrypted += chr((ord(i) + 26) - shift)
            else:
                decrypted += chr(ord(i) - shift)
        else:
            decrypted += i
    return decrypted

def get_user_info():
    user_phrase = input('Enter a (breif) text to encrypt: ')
    shift = int(input('Enter the number to shift the letters by: '))
    return user_phrase, shift

menu()
menu_choice = input('Enter your selection: ')

while menu_choice.upper() != 'Q':
    if menu_choice == '1':
        user_phrase, shift = get_user_info()
        print(encrypt(user_phrase, shift))
    elif menu_choice == '2':
        user_phrase, shift = get_user_info()
        print(decrypt(user_phrase, shift))
    else:
        print('Please input 1, 2, or Q')
    print()
    menu()
    menu_choice = input('Enter your selection: ')
print('Have An Extraordinary Day!!!')
    