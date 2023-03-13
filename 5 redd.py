#!/usr/bin/env python

import sys

#Output: address[0]
#Noun: address[1]
#Verb:  address[2]
#Add: opcode 1
#Multiply: opcode 2
#Input: opcode 3
#Output: opcode 4

#noun = 0
#verb = 0

def execute_add(intcode, mode, pointer):
    if mode[0] == 0:
        param1 = int(intcode[intcode[pointer +1]])
    elif mode[0] == 1:
        param1 = int(intcode[pointer +1])
    if mode[1] == 0:
        param2 = int(intcode[intcode[pointer +2]])
    elif mode[1] == 1:
        param2 = int(intcode[pointer +2])
    param3 = int(intcode[pointer +3])
    intcode[param3] = param1 + param2
    pointer += 4
    return intcode,pointer

def execute_multiply(intcode, mode, pointer):
    if mode[0] == 0:
        param1 = int(intcode[intcode[pointer +1]])
    elif mode[0] == 1:
        param1 = intcode[pointer +1]
    if mode[1] == 0:
        param2 = int(intcode[intcode[pointer +2]])
    elif mode[1] == 1:
        param2 = int(intcode[pointer +2])
    param3 = int(intcode[pointer +3])
    intcode[param3] = param1 * param2
    pointer += 4
    return intcode,pointer

def execute_input(intcode, mode, pointer):
    print("Input:")
    user_input = input()
    param1 = int(intcode[pointer + 1])
    intcode[param1] = int(user_input.strip())
    pointer += 2
    return intcode,pointer

def execute_output(intcode, mode, pointer):
    param1 = int(intcode[intcode[pointer + 1]])
    intcode[0] = param1
    pointer += 2
    return intcode,pointer

def execute_halt(intcode):
    print(intcode[0])
    sys.exit()

def parse_opcode(intcode,pointer):
    instruction = intcode[pointer]
    instruction_length = len(str(instruction))
    if instruction_length > 1:
        opcode = int(str(instruction)[instruction_length -2:instruction_length])
    else:
        opcode = int(instruction)
    if instruction_length > 2:
        mode_1 = int(str(instruction)[instruction_length-3:instruction_length-2])
        if instruction_length > 3:
            mode_2 = int(str(instruction)[instruction_length-4:instruction_length-3])
            if instruction_length > 4:
                mode_3 = int(str(instruction)[instruction_length-1])
            else:
                mode_3 = 0
        else:
            mode_2 = 0
            mode_3 = 0
    else:
        mode_1 = 0
        mode_2 = 0
        mode_3 = 0
    if opcode == 1:
        intcode,pointer = execute_add(intcode, [mode_1, mode_2, mode_3], pointer)
    elif opcode == 2:
        intcode,pointer = execute_multiply(intcode, [mode_1, mode_2, mode_3], pointer)
    elif opcode == 3:
        intcode,pointer = execute_input(intcode, [mode_1, mode_2, mode_3], pointer)
    elif opcode == 4:
        intcode,pointer = execute_output(intcode, [mode_1, mode_2, mode_3], pointer)
    elif opcode == 99:
        intcode,pointer = execute_halt(intcode)
    return intcode,pointer



instructioninput = open("5.in", "r")
intcode = instructioninput.read().split(",")
intcode = [ int(x) for x in intcode ]
pointer = 0
while True:
    intcode,pointer = parse_opcode(intcode, pointer)
    print(intcode[0])