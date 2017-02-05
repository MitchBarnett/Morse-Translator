

# necessary module imports
import winsound
import sys
from time import sleep

# The Morse Code alphabet to translate to and from
morse_alph_a = {
    'A': '.-',       'B': '-...',     'C': '-.-.',     'D': '-..',
    'E': '.',        'F': '..-.',     'G': '--.',      'H': '....',
    'I': '..',       'J': '.---',    'K': '-.-',       'L': '.-..',
    'M': '--',       'N': '-.',       'O': '---',      'P': '.--.',
    'Q': '--.-',     'R': '.-.',      'S': '...',      'T': '-',
    'U': '..-',      'V': '...-',     'W': '.--',      'X': '-.--',
    'Y': '-.--',     'Z': '--..',     '0': '-----',    '1': '.----',
    '2': '..---',    '3': '...--',    '4': '....-',    '5': '.....',
    '6': '-....',    '7': '--....',   '8': '---..',    '9': '----.',
    '.': '.-.-.-',   ',': '--..--',   ':': '---...',   '?': '..--..',
    "'": '.----.',   '-': '-....-',   '//': '-..-.',   '(': '-.--.-',
    ')': '-.--..',   '"': '.-..-.',   '@': '.--.-.',   '=': '-...-',   ' ': ' '
}

morse_alph_b = dict(zip(morse_alph_a.values(), morse_alph_a
                        .keys()))

#
# Begin defining function's                     #
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

    choice = input('Option:')

    if choice == '1':
        morse_code = translate_from_file()
        print(morse_code)
        play_morse(morse_code)
        to_write = input(
            'Do you want to write this Morse code to a text file?').lower()
        if to_write == 'yes' or to_write == 'y':
            print('RAN')
            write_to_file(morse_code)

    elif choice == '2':
        morse_code = translate_directly()
        print(morse_code)
        play_morse(morse_code)
        to_write = input(
            'Do you want to write this morse code to a text file?').lower()
        if to_write == 'yes' or to_write == 'y':
            write_to_file(morse_code)

    elif choice == '9':
        quit()

    else:
        print('invalid choice')
        menu()


def detect_translate(user_input):
    """
    Summary: Decides if a user input is in Morse code or not


    Arguments: user_input - the users inputed string

    Returns: morse or english
    """
    dit_dar_count = 0
    for i in user_input:
        if i == '-' or i == '.':
            dit_dar_count += 1
    print('dit_dar_count =',dit_dar_count)
    print(len(user_input) / 2)
    if len(user_input) / 2 < dit_dar_count:
        return 'morse'
    else:
        return 'english'


def translate_from_file():
    # read_from_file is ran then verified this information is passed to the
    # translate function.
    user_input = read_from_file()

    if verify_input(user_input):
        print('You tried to translate Invalid characters')
        translate_from_file()
    else:
        pass
    return (translate(user_input, detect_translate()))


def translate_directly():
    # get_user_input is ran this information is verified and passed to the
        # translate function
        user_input = get_user_input()

        if verify_input(user_input):
            print('You tried to translate Invalid characters')
            translate_from_file()
        else:
            pass
        return (translate(user_input, detect_translate(user_input)))


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
    user_input = input('Enter text to be translated:')
    return user_input.upper()


def verify_input(user_input):
    test_bool = False
    for char in user_input:
        if char in morse_alph_a:
            pass
        else:
            test_bool = True
            break
    return test_bool


def translate(user_input, type):
    string = ''
    if type == 'english':
        for letter in user_input:
            string += morse_alph_a[letter]
            string += ' '
    elif type == 'morse':
        for letter in user_input:
            string += morse_alph_b[letter]
            string += ' '
    else:
        raise NameError('invalid type in translate function')
    return(string)


def play_morse(morse_code):
    for char in morse_code:
        if char is '.':
            winsound.Beep(700, 100)
        elif char is '-':
            winsound.Beep(700, 300)
        elif char is '/':
            sleep(0.2)
    sleep(0.05)


def write_to_file(morse_code):
    print('NOTE: IF YOU HAVE A FILE WITH THE SAME NAME IT WILL BE \n\
        OVERWTITTEN IF YOU DON\'T THE FILE WILL BE CREATED')
    filename = input('Enter the filename to write to: ').lower()
    if filename[-4:] != '.txt':
        filename += '.txt'
    f = open(filename, 'w')
    print(morse_code)
    user_input = f.write(morse_code)
    f.close()


def main():
    while True:
        menu()


if __name__ == '__main__':
    main()
