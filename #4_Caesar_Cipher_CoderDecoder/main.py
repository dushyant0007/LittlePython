import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo.logo)


def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


start()


def encrypt(plainText, shiftAmount):
    cipher_text = ""
    shiftAmount = shiftAmount % 26
    for letter in plainText:
        position = alphabet.index(letter)
        new_position = position + shiftAmount
        new_letter = alphabet[new_position]
        cipher_text = cipher_text + new_letter

    print(f"The encoded text is {cipher_text}")


def decrypt(plainText, shiftAmount):
    cipher_text = ""
    shiftAmount = shiftAmount % 26
    for letter in plainText:
        position = alphabet.index(letter)
        new_position = position - shiftAmount
        new_letter = alphabet[new_position]
        cipher_text = cipher_text + new_letter

    print(f"The encoded text is {cipher_text}")


play = True

while play:

    if direction == 'encode':
        encrypt(text, shift)

    else:
        decrypt(text, shift)
