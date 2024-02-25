MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    cipher = ''
    for letter in message.upper():
        if letter != ' ':
            cipher += f'{MORSE_CODE_DICT[letter]} '
    return cipher

def decrypt(cipher):
    message = ''
    cipher_list = cipher.split(' ')
    for char in cipher_list:
        for key in MORSE_CODE_DICT:
            if MORSE_CODE_DICT[key] == char:
                message += key

    return message
def translate():
    message = ''
    while len(message) < 1:
        message = input("Your message (decrypting will output message without spaces): ")
    char_counter = 0
    for char in message:
        if char == '.' or char == '-':
            char_counter +=1
    if char_counter/len(message) > 0.5:
        print(decrypt(message))
    else:
        print(encrypt(message))

translate()
