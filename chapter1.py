import string


def create_shift_substitutions(n):
	encoding = {}
	decoding = {}

	alphabet_size = len(string.ascii_uppercase)

	for i in range(alphabet_size):
		letter = string.ascii_uppercase[i]
