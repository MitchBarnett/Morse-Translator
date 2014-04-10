
# necessary module imports
import winsound
import sys
from time import sleep

# The Morse Code alphabet to translate to and from
morse_alph = {
    'A': '.-',       'B': '-...',     'C': '-.-.',     'D': '-..',      'E': '.',
    'F': '..-.',     'G': '--.',      'H': '....',     'I': '..',       'J': '.---',
    'K': '-.-',      'L': '.-..',     'M': '--',       'N': '-.',       'O': '---',
    'P': '.--.',     'Q': '--.-',     'R': '.-.',      'S': '...',      'T': '-',
    'U': '..-',      'V': '...-',     'W': '.--',      'X': '-.--',     'Y': '-.--',
    'Z': '--..',     '0': '-----',    '1': '.----',    '2': '..---',    '3': '...--',
    '4': '....-',    '5': '.....',    '6': '-....',    '7': '--....',   '8': '---..',
    '9': '----.',    ' ': '/',        '.': '.-.-.-',   ',': '--..--'
}


#
# Begin defining function's
#


def menu():
    """
    Summary: Presents the user with a menu giving the option of a
             direct translation, translation from a file, or quiting. If there
             is an invalid input the function will be called again so the user
             can make another selection


    Arguments: None

    Returns: None


    """
    print('Do you want to:\n\
        1) Translate from a file\n\
        2) Translate from direct input\n\
        9) quit the program')
    choice = input('input')

    if choice is '1':
        translate_from_file()

    elif choice is '2':
        # get_user_input is ran this information is verified and passed to the
        # translate function

        verified_input = get_user_input(verify_input())
        translate(verify_input)
    elif choice is '9':
        sys.exit()

    else:
        print('invalid choice')
        menu()


def translate_from_file():
    # read_from_file is ran then verified this information is passed to the
    # translate function.
    user_input = read_from_file()
    
    if verify_input(user_input):
        print('You tried to translate Invalid characters')
        translate_from_file()
    else:
        pass
    print(translate(user_input))


def read_from_file():
    """
    Summary: Prompts the user to enter a filename. The last 4 char's are
             checked to see if they are .txt if they are not .txt is appended
             to the end. This sets the f variable and the file is read and the
             value stored in user_input. This is then capitalized and returned.


    Arguments: None

    Returns: user_input(An Upper case string)

    """
    print('NOTE: FILE MUST BE IN SAME DIRECTORY AS THIS PROGRAM')
    filename = input('Enter the filename to read from: ').lower()
    if filename[-4:] != '.txt':
        filename += '.txt'
    f = open(filename, 'r')
    user_input = f.read()
    f.close()
    return user_input.upper()


def get_user_input():
    user_input = input('Enter text to be translated')


def verify_input(user_input):
    test_bool = False
    for char in user_input:
        if char in morse_alph:
            pass
        else:
            test_bool = True
            break
    return test_bool


def translate(user_input):
    string = ''
    for letter in user_input:
        string += morse_alph[letter]
        string += ' '
    return(string)


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
                    winsound.Beep(700, 200)
                elif i == '-':
                    winsound.Beep(700, 600)
                else:
                    sleep(0.2)

# while True:
#    output(input('enter a word: ').upper())
