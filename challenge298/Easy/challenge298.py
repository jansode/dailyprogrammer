import sys

def get_extra_paren_indices(string):

    right_parens = []
    remove_parens = []     
    expressions = []    #start indices of expressions
    expr_found = False 

    for index, char in enumerate(string):
        if char == '(':
            right_parens.append(index)
            expr_found = False

        elif char == ')':
            if len(expressions) > 0 and right_parens[-1] < expressions[-1] < index:
                expressions.pop()
                right_parens.pop()
                expr_found = False
            else:
                remove_parens.append(right_parens.pop())
                remove_parens.append(index)
        elif not expr_found:
            expressions.append(index) 
            expr_found = True

    return remove_parens 

def remove_parens(string, indices):
    result = []
    for index, char in enumerate(string):
        if index not in indices:
            result.append(char)

    return ''.join(result)

def main():
    for string in sys.argv[1:]:
        result = remove_parens(string, get_extra_paren_indices(string))

        if result == '':
            print "NULL"
        else:
            print result

if __name__ == '__main__':
    main()
