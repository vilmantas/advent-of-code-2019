from enum import IntEnum
from typing import List

data = [int(x) for x in open('input-5.txt', 'r').read().split(',')] 

def get_parameters(metadata: str, parameters_count: int, metadata_index: int):

    result =[]

    metadata = metadata[::-1][2:]

    for i in range(1, parameters_count + 1):

        if i  > len(metadata):
            parameter_code = ''
        else:
            parameter_code = metadata[i - 1]

        if parameter_code == '' or parameter_code == '0':
            location = data[metadata_index + i]
            value = data[location]
        else:
            value = data[metadata_index + i]

        result.append(value)

    return result

class ParameterCode(IntEnum):
    POSSITION = 0
    IMMEDIATE = 1

class OperationCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    STORE_INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    STOP = 99

class OperationParameter(object):

    value: int
    code: ParameterCode

    def __init__(self, value: int, code: ParameterCode):
        self.value = value
        self.code = code

    def __repr__(self):
        return f'{self.code.name}, {self.value}'

class Operation(object):

    code: OperationCode
    parameters: List[OperationParameter]

    def __init__(self, code: OperationCode, parameters: List[OperationParameter]):
        self.code = code
        self.parameters = parameters

if __name__ == "__main__":

    op_index = 0

    while True:
        op_data = str(data[op_index])
        op_code = int(op_data[-1:])

        if op_code == OperationCode.ADD:

            first, second = get_parameters(op_data, 2, op_index)
            
            result_location = data[op_index + 3]

            data[result_location] = first + second

            op_index += 4

        elif op_code == OperationCode.MULTIPLY:

            first, second = get_parameters(op_data, 2, op_index)
            
            result_location = data[op_index + 3]

            data[result_location] = first * second

            op_index += 4

        elif op_code == OperationCode.STORE_INPUT:

            result_index = data[op_index + 1]

            data[result_index] = 5

            op_index += 2

        elif op_code == OperationCode.OUTPUT:
            
            location = data[op_index + 1]

            print(data[location])

            op_index += 2

        elif op_code == OperationCode.JUMP_IF_TRUE:

            first, second = get_parameters(op_data, 2, op_index)

            if first != 0: 
                op_index = second
            else: 
                op_index += 3

        elif op_code == OperationCode.JUMP_IF_FALSE:

            first, second = get_parameters(op_data, 2, op_index)

            if first == 0:
                op_index = second
            else: 
                op_index += 3

        elif op_code == OperationCode.LESS_THAN:

            first, second = get_parameters(op_data, 2, op_index)

            location = data[op_index + 3]

            if first < second:
                data[location] = 1
            else:
                data[location] = 0

            op_index += 4

        elif op_code == OperationCode.EQUALS:

            first, second = get_parameters(op_data, 2, op_index)

            location = data[op_index + 3]

            if first == second:
                data[location] = 1
            else:
                data[location] = 0

            op_index += 4

        elif int(op_data[-2:]) == OperationCode.STOP:
            break;
    pass