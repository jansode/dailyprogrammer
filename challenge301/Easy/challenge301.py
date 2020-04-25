import sys

def filter_pattern(word, pattern):
    num_states = len(pattern)
    curr_state = 0
    dictionary = {}
    for index,char in enumerate(word):
        for check_char in word[index:]:
            if curr_state == num_states-1:
                print("in true")
                return True

            if char == '\n':
                break

            if pattern[curr_state] in dictionary:
                if dictionary[pattern[curr_state]] == check_char:
                    curr_state+=1
                    continue
                else:
                    curr_state = 0
                    dictionary.clear()
                    dictionary.update({pattern[curr_state]:char})
                    break

            dictionary.update({pattern[curr_state]:check_char})


    return False

def read_dict(dictionary_file,pattern):
    matches = []
    with open(dictionary_file) as f:
        word = f.read()
        if filter_pattern(word,pattern):
            matches.append(word)

    return matches

def main():
    if len(sys.argv) < 3:
        print("Missing arguments")
        exit(1)

    pattern = sys.argv[1]
    dictionary_file = sys.argv[2]

    matches = read_dict(dictionary_file, pattern)

    for word in matches:
        print(word)

if __name__ == '__main__':
    main()
