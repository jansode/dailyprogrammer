import sys

def draw_histogram(x_start, x_end, y_start, y_end, intervals, frequencies):
    print_rest = []
    for i in range(y_end, y_start, -1):
        print(i, end='')
        for j in range(len(intervals)):
            if intervals[j] in frequencies[i] or print_rest[j]:
                print('*', end='')
                if j not in print_rest:
                    print_rest.append(j)

def main():
    dimensions = input().split()
    if len(dimensions) != 4:
        print("Incorrect dimensions")
        return

    x_start = int(dimensions[0])
    x_end   = int(dimensions[1])
    y_start = int(dimensions[2])
    y_end   = int(dimensions[3])

    num_intervals = eval(input())

    intervals = []

    #A list of all the interval indices that reach a given frequency
    frequencies = [[]*num_intervals]

    for i in range(num_intervals):
        input_row = input().split()
        if len(input_row) != 3:
            print("Incorrect size on input row")
            return

        #I assume the intervals are given in order
        intervals.append([int(input_row[0]),int(input_row[1])])

        frequencies[int(input_row[2])].append(i)

    draw_histogram(x_start, x_end, y_start, y_end, intervals, frequencies)

if __name__ == '__main__':
    main()
