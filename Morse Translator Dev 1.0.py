import winsound
import sys
from time import sleep
morse_alph = {
    'A':'.-',       'B':'-...',     'C':'-.-.',     'D':'-..',      'E':'.',
    'F':'..-.',     'G':'--.',      'H':'....',     'I':'..',       'J':'.---',
    'K':'-.-',      'L':'.-..',     'M':'--',       'N':'-.',       'O':'---',
    'P':'.--.',     'Q':'--.-',     'R':'.-.',      'S':'...',      'T':'-',
    'U':'..-',      'V':'...-',     'W':'.--',      'X':'-.--',     'Y':'-.--',
    'Z':'--..',     '0':'-----',    '1':'.----',    '2':'..---',    '3':'...--',
    '4':'....-',    '5':'.....',    '6':'-....',    '7':'--....',   '8':'---..',
    '9':'----.',    ' ':'/',        '.':'.-.-.-',   ',':'--..--'
    }

def read_from_file():
    print('NOTE: FILE MUST BE IN SAME DIRECTORY AS THIS PROGRAM')
    filename = input('Enter the filename to read from: ').lower()
    if filename[-4:] != '.txt':
        filename += '.txt'
    f= open(filename,'r') 
    user_input = f.read()
    return user_input.upper()

def menu():
    print('Do you want to:\n\
        1) Translate from a file\n\
        2) Tranlate from direct input\n\
        9) quit the program')
    choice = input('input')

    if choice is '1':
        translate_input(read_from_file())
    elif choice is '2':
        print('Translate directly confirmed')
    elif choice is '9':
        sys.exit()
    else:
        print('invalid choice')



    

def verify_input():
    pass


def translate_input(user_input):
    string = ''
    for letter in user_input:
        string += morse_alph[letter]
        string += ' '
    print(string)


def play_morse():
    pass


def write_morse():
    pass


def main():
    while True:
        menu()


if __name__ == '__main__':
    main()
    

def output(string):
    for char in string:
        morse = morse_alph[char]
        for i in morse:
                if i == '.':
                    winsound.Beep(700,200)
                elif i == '-':
                    winsound.Beep(700,600)
                else:
                    sleep(0.2)

#while True:
#    output(input('enter a word: ').upper())
    
