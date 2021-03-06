import string
import sys

s1 = set(string.punctuation)
s2 = set(string.digits)
s3 = set(string.ascii_lowercase)
s4 = set(string.ascii_uppercase)
classes = [s1, s2, s3, s4]

def countclasses(password):
	pset = set(password)
	count = 0
	for c in classes:
		if pset & c:
			count += 1
	return count

def main():
	for line in sys.stdin:
		print(countclasses(line))

if __name__ == '__main__':
	main()
