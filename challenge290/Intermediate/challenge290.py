import sys

leds = [False] * 8
a_reg = 0

def do_command(command_string): 
    opcode, value = command_string.split(',')

    if opcode == 'ld a':
        a_reg = int(value)
    elif opcode == 'out (0)':
        for i in "{0:b}".format(int(value)):
            if i == '1':
                print '*',
            else:
                print '.',

        
def parse_file(path):
    with open(path, 'r') as f:
        file_data = f.read()

    for line_num, line in enumerate(file_data):
        if line == '':
            continue

        for index, char in enumerate(line):
            if char == ' ':
                continue

            do_command(line[index:])

def main():
    parse_file(sys.argv[1])

if __name__ == '__main__':
    main()
