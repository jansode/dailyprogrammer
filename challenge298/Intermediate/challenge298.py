import sys

def get_unbalanced_paren_index(string):
    stack = [] 
    for index, char in enumerate(string):
        if char == '(':
            stack.append(index)
        elif char == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return index 

    if len(stack) > 0:
        return stack[0]
    else:
        return len(string)

def main():
    for string in sys.argv[1:]:
        index = get_unbalanced_paren_index(string)

        if(index == len(string)):
            print string
        else:
            print string[:index] + '**' + string[index] + '**' + string[index+1:]

if __name__ == '__main__':
    main()

