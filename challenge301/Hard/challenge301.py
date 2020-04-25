import sys

notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

#the open strings
tuning = []


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

def main():
    if len(sys.argv) < 2):
        print("Missing arguments")
        sys.exit(1)

    data = read_file(sys.argv[1])
    parse_tuning(data)

if __name__ == '__main__':
    main()

