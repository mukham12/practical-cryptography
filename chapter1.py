import string


def create_shift_substitutions(n):
	encoding = {}
	decoding = {}

	alphabet_size = len(string.ascii_uppercase)

	for i in range(alphabet_size):
		letter = string.ascii_uppercase[i]
		subst_letter = string.ascii_uppercase[(i + n) % alphabet_size]

		encoding[letter] = subst_letter
		decoding[subst_letter] = letter

	return encoding, decoding


def encode(message, subst):
	cipher = ''
	for letter in message:
		if letter in subst:
			cipher += subst[letter]
		else:
			cipher += letter

	return cipher

def decode(message, subst):
    return encode(message, subst)

def printable_subst(subst):
    mapping = sorted(subst.items())
    alphabet_line = " ".join(letter for letter, _ in mapping)
    cipher_line = " ".join(subst_letter for _, subst_letter in mapping)
    return f'{alphabet_line}\n{cipher_line}'

if __name__ == 'main':
    n = 1
    encoding, decoding = create_shift_substitutions(n)
    while True:
        print('\nShift Encoder Decoder')
        print('--------------------')
        print(f'\tCurrent Shift {n}\n')
        print('\t1. Print Encoding/Decoding tables.')
        print('\t2. Encode message.')
        print('\t3. Decode message.')
        print('\t4. Change shift.')
        print('\t5. Quit.')
        choice = input('>> ')
        print()

        if choice == '1':
           print('Encoding table: ')
           print(printable_subst(encoding))
           print('Decoding table: ')
           print(printable_subst(decoding))
        elif choice == '2':
           message = input('\nMessage to encode: ')
           print(f'Encoded message is {encode(message.upper(), encoding)}')
        elif choice == '3':
           pass
