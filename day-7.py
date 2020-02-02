from enum import IntEnum
from typing import List

import itertools

data = [int(x) for x in open('input-7.txt', 'r').read().split(',')] 

def get_parameters(metadata: str, parameters_count: int, metadata_index: int, input_data: []):

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
        else:
            value = input_data[metadata_index + i]

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

class Amplifier(object):

    def __init__(self, data, input):
        self.data = data
        self.inputs = input
        self.op_index = 0
        self.outputs = []
        self.terminated = False
        self.requires_input = False


    def Process(self):

        op_data = str(self.data[self.op_index])
        op_code = int(op_data[-1:])

        if op_code == OperationCode.ADD:

            first, second = get_parameters(op_data, 2, self.op_index, self.data)
            
            result_location = self.data[self.op_index + 3]

            self.data[result_location] = first + second

            self.op_index += 4

        elif op_code == OperationCode.MULTIPLY:

            first, second = get_parameters(op_data, 2, self.op_index, self.data)
            
            result_location = self.data[self.op_index + 3]

            self.data[result_location] = first * second

            self.op_index += 4

        elif op_code == OperationCode.STORE_INPUT:

            result_index = self.data[self.op_index + 1]

            if len(self.inputs) == 0:
                self.requires_input = True
                return

            data = self.inputs.pop(0)

            self.data[result_index] = data

            self.op_index += 2

        elif op_code == OperationCode.OUTPUT:
            
            location = self.data[self.op_index + 1]
            
            self.outputs.append(self.data[location])

            self.op_index += 2

        elif op_code == OperationCode.JUMP_IF_TRUE:

            first, second = get_parameters(op_data, 2, self.op_index, self.data)

            if first != 0: 
                self.op_index = second
            else: 
                self.op_index += 3

        elif op_code == OperationCode.JUMP_IF_FALSE:

            first, second = get_parameters(op_data, 2, self.op_index, self.data)

            if first == 0:
                self.op_index = second
            else: 
                self.op_index += 3

        elif op_code == OperationCode.LESS_THAN:

            first, second = get_parameters(op_data, 2, self.op_index, self.data)

            location = self.data[self.op_index + 3]

            if first < second:
                self.data[location] = 1
            else:
                self.data[location] = 0

            self.op_index += 4

        elif op_code == OperationCode.EQUALS:

            first, second = get_parameters(op_data, 2, self.op_index, self.data)

            location = self.data[self.op_index + 3]

            if first == second:
                self.data[location] = 1
            else:
                self.data[location] = 0

            self.op_index += 4

        elif int(op_data[-2:]) == OperationCode.STOP:
            self.terminated = True
        
if __name__ == "__main__":

    max = -23554

    for i in perms:
        sequence = i

        first_a = Amplifier(data.copy(), [sequence[0], 0])

        second_a = Amplifier(data.copy(), [sequence[1]])

        third_a = Amplifier(data.copy(), [sequence[2]])

        fourth_a = Amplifier(data.copy(), [sequence[3]])

        fifth_a = Amplifier(data.copy(), [sequence[4]])

        while True:

                if fifth_a.terminated:
                    print(fifth_a.outputs)
                    break;

                while not first_a.terminated:

                    if first_a.requires_input:
                        if len(fifth_a.outputs) is not 0:
                            first_a.inputs.append(fifth_a.outputs.pop(0))
                            first_a.requires_input = False
                        else:
                            break;

                    first_a.Process()


                while not second_a.terminated:

                    if second_a.requires_input:
                        if len(first_a.outputs) is not 0:
                            second_a.inputs.append(first_a.outputs.pop(0))
                            second_a.requires_input = False
                        else:
                            break;

                    second_a.Process()

                while not third_a.terminated:

                    if third_a.requires_input:
                        if len(second_a.outputs) is not 0:
                            third_a.inputs.append(second_a.outputs.pop(0))
                            third_a.requires_input = False
                        else:
                            break;

                    third_a.Process() 

                while not fourth_a.terminated:

                    if fourth_a.requires_input:
                        if len(third_a.outputs) is not 0:
                            fourth_a.inputs.append(third_a.outputs.pop(0))
                            fourth_a.requires_input = False
                        else:
                            break;

                    fourth_a.Process()

                while not fifth_a.terminated:

                    if fifth_a.requires_input:
                        if len(fourth_a.outputs) is not 0:
                            fifth_a.inputs.append(fourth_a.outputs.pop(0))
                            fifth_a.requires_input = False
                        else:
                            break;

                    fifth_a.Process()      

                result = fifth_a.outputs  

        r = result.pop()

        if r > max:
            max = r

    print(max)
    pass