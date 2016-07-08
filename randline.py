import random
import sys

def main():
    lines = open(sys.argv[1]).readlines()
    print(lines[random.randrange(len(lines))])


if __name__ == "__main__":
    main()