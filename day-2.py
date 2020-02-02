
# First part
def work(in1: int, in2: int): 

    input = [1,12,2,3,
    1,1,2,3,
    1,3,4,3,
    1,5,0,3,
    2,1,9,19,
    1,19,5,23,
    2,23,13,27,
    1,10,27,31,
    2,31,6,35,
    1,5,35,39,
    1,39,10,43,
    2,9,43,47,
    1,47,5,51,
    2,51,9,55,
    1,13,55,59,
    1,13,59,63,
    1,6,63,67,
    2,13,67,71,
    1,10,71,75,
    2,13,75,79,
    1,5,79,83,2,
    83,9,87,2,87,
    13,91,1,91,5,
    95,2,9,95,99,
    1,99,5,103,1,
    2,103,107,1,
    10,107,0,99,
    2,14,0,0]

    index = 0
    value = 1
    
    for i in range(0, input.__len__()):

        input[1] = in1
        input[2] = in2

        value = input[index]

        if value is 99:
            return input[0]
        
        first = input[index + 1]
        second = input[index + 2]
        result_loc = input[index + 3]

        if value is 1:
            result = input[first] + input[second]

        if value is 2:
            result = input[first] * input[second]

        input[result_loc] = result
        index = index + 4

    return input[0]

if __name__ == "__main__":
    result = -1
    incrementFirst = True

    first = 64
    second = 100
    # Second part
    while result != 19690720:
        result = work(first, second)

        print(f'first: {first}')
        print(f'second {second}')
        print(f'result {result}')

        if incrementFirst:
            second -= 1
        else:
            second -= 1
        incrementFirst = not incrementFirst




    pass