import random

def deterministicNumber():
	'''
	Deterministically generates and returns an even number between 9 and 21
	'''
	for i in range(9, 21):
		if i % 2 == 0:
			return i

if __name__ == '__main__':
	print(deterministicNumber())
