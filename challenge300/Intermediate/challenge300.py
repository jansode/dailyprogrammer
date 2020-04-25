import sys

def print_tape(tape):
    for cell in tape:
        if cell == 1:
            print('*',end='')
        else:
            print(' ', end='')
    print('\n')

def main():
    if len(sys.argv) < 4:
        print("Missing arguments")
        sys.exit(1)

    tape_size = int(sys.argv[1])
    rows = int(sys.argv[2])
    rule = int(sys.argv[3])

    #The initial tape list. The middle value always starts out as 1. 
    tape = [0] * tape_size 
    tape[int(tape_size/2)] = 1

    #A list for the next generation values that will be generated
    next_gen = [0] * tape_size

    for row in range(rows-1):
        print_tape(tape)
        for index, cell in enumerate(tape):

            left = tape[(index-1)%tape_size]
            right = tape[(index+1)%tape_size]

            #check both neighbors set
            if left == 1 and right == 1:
                rule_bit = 0x80 if cell == 1 else 0x20
                next_gen[index] = 1 if (rule & rule_bit) > 0 else 0 
            #check left neighbor set
            elif left == 1 and right == 0: 
                rule_bit = 0x40 if cell == 1 else 0x10
                next_gen[index] = 1 if (rule & rule_bit) > 0 else 0
            #check right neighbor set
            elif left == 0 and right == 1: 
                rule_bit = 0x8 if cell == 1 else 0x2
                next_gen[index] = 1 if (rule & rule_bit) > 0 else 0
            #check both neighbors unset
            elif left == 0 and right == 0: 
                rule_bit = 0x4 if cell == 1 else 0x1 
                next_gen[index] = 1 if (rule & rule_bit) > 0 else 0

        tape = next_gen[:]

if __name__ == '__main__':
    main()
