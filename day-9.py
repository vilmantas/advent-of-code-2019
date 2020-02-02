from enum import IntEnum
from typing import List

import itertools

data = [int(x) for x in open('input-9.txt', 'r').read().split(',')] 

for i in range(1000):
    data.append(0)

def get_parameters(metadata: str, parameters_count: int, metadata_index: int, input_data: [], relative_base: int = 0):

    result =[]

    metadata = metadata[::-1][2:]

    for i in range(1, parameters_count + 1):

        if i  > len(metadata):
            parameter_code = ''
        else:
            parameter_code = metadata[i - 1]

        if parameter_code == '' or parameter_code == '0':
            location = input_data[metadata_index + i]
            value = input_data[location]
        elif parameter_code == '1':
            value = input_data[metadata_index + i]
        elif parameter_code == '2':
            location = input_data[metadata_index + i]
            value = input_data[relative_base + location]
        result.append(value)

    return result

def get_location(metadata: str, param_count: int, data: [], index: int, base: int):
    if len(metadata) != param_count + 2:
        result_location = data[index  + param_count]
    elif int(metadata[0]) == 1:
        result_location = index + param_count
    elif int(metadata[0]) == 2:
        result_location = data[index + param_count] + base
    
    return result_location

class OperationCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    STORE_INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_BASE = 9
    STOP = 99

class Amplifier(object):

    def __init__(self, data, input):
        self.data = data
        self.inputs = input
        self.op_index = 0
        self.outputs = []
        self.terminated = False
        self.requires_input = False
        self.base = 0


    def Process(self):

        op_data = str(self.data[self.op_index])
        op_code = int(op_data[-1:])

        if op_code == OperationCode.ADD:

            first, second = get_parameters(op_data, 2, self.op_index, self.data, self.base)
            
            location = get_location(op_data, 3, self.data, self.op_index, self.base)

            self.data[location] = first + second

            self.op_index += 4

        elif op_code == OperationCode.MULTIPLY:

            first, second = get_parameters(op_data, 2, self.op_index, self.data, self.base)
            
            location = get_location(op_data, 3, self.data, self.op_index, self.base)

            self.data[location] = first * second

            self.op_index += 4

        elif op_code == OperationCode.STORE_INPUT:

            data = self.inputs.pop(0)

            location = get_location(op_data, 1, self.data, self.op_index, self.base)

            self.data[location] = data

            self.op_index += 2

        elif op_code == OperationCode.OUTPUT:
            
            value = get_parameters(op_data, 1, self.op_index, self.data, self.base)
            
            self.outputs.append(value)

            self.op_index += 2

        elif op_code == OperationCode.JUMP_IF_TRUE:

            first, second = get_parameters(op_data, 2, self.op_index, self.data, self.base)

            if first != 0: 
                self.op_index = second
            else: 
                self.op_index += 3

        elif op_code == OperationCode.JUMP_IF_FALSE:

            first, second = get_parameters(op_data, 2, self.op_index, self.data, self.base)

            if first == 0:
                self.op_index = second
            else: 
                self.op_index += 3

        elif op_code == OperationCode.LESS_THAN:

            first, second = get_parameters(op_data, 2, self.op_index, self.data, self.base)

            location = get_location(op_data, 3, self.data, self.op_index, self.base)

            if first < second:
                self.data[location] = 1
            else:
                self.data[location] = 0

            self.op_index += 4

        elif op_code == OperationCode.EQUALS:

            first, second = get_parameters(op_data, 2, self.op_index, self.data, self.base)

            location = get_location(op_data, 3, self.data, self.op_index, self.base)

            if first == second:
                self.data[location] = 1
            else:
                self.data[location] = 0

            self.op_index += 4

        elif int(op_data[-2:]) == OperationCode.STOP:
            self.terminated = True

        elif op_code == OperationCode.ADJUST_BASE:

            value = get_parameters(op_data, 1, self.op_index, self.data, self.base)
            
            self.base += value[0]

            self.op_index += 2


        
if __name__ == "__main__":

    first_a = Amplifier(data.copy(), [2])

    while not first_a.terminated:
        first_a.Process()

    print(first_a.outputs)

    pass