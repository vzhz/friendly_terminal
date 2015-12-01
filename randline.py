import random, sys

def main():
	lines = open(sys.argv[1]).readlines()
	print (lines[random.randrange(len(lines))])


if __name__ == "__main__":
	main()
#from http://stackoverflow.com/questions/448005/whats-an-easy-way-to-read-random-line-from-a-file-in-unix-command-line/448021#448021
#note: written in python3