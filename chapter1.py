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

