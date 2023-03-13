from itertools import permutations
from Amplifier import Amplifier

nums = open('7.in').read().split(',')
prog = []
for num in nums:
    prog.append(int(num))


def amp(prog, input):
    i = 0
    cnt = 0
    while True:
        opcode     = prog[i] % 100
        param1mode = prog[i] // 100 % 10
        param2mode = prog[i] // 1000 % 10
        param3mode = prog[i] // 10000 % 10
        if opcode in [1, 2, 5, 6, 7, 8]:
            if param1mode == 0:
                idx1 = prog[i + 1]
                op1 = prog[idx1]
            else:
                op1 = prog[i + 1]
            if param2mode == 0:
                idx2 = prog[i + 2]
                op2 = prog[idx2]
            else:
                op2 = prog[i + 2]

        match opcode:
            case 1:
                idx3 = prog[i + 3]
                prog[idx3] = op1 + op2
                i += 4
            case 2:
                idx3 = prog[i + 3]
                prog[idx3] = op1 * op2
                i += 4
            case 3:
                idx1 = prog[i + 1]
                prog[idx1] = input[cnt]
                cnt += 1
                i += 2
            case 4:
                if param1mode == 0: 
                    idx1 = prog[i + 1]
                    op1 = prog[idx1]
                else:
                    op1 = prog[i + 1]
                return op1
                i += 2
            case 5: #jump-if-true
                if op1 != 0:
                    i = op2
                    continue
                else:
                    i += 3
            case 6: #jump-if-false
                if op1 == 0:
                    i = op2
                    continue
                else:
                    i += 3
            case 7: #less than
                idx3 = prog[i + 3]
                if op1 < op2:
                    prog[idx3] = 1
                else:
                    prog[idx3] = 0
                i += 4
            case 8: #equals
                idx3 = prog[i + 3]
                if op1 == op2:
                    prog[idx3] = 1
                else:
                    prog[idx3] = 0
                i += 4
            case 99:
                break
            case _:
                i += 1
                continue




def part1():
    perm = permutations([0, 1, 2, 3, 4])
    maxim = 0
    for p in perm:
        inputSignal = 0
        for i in range(5):
            inputSignal = amp(list(prog), [p[i], inputSignal]) 
        if inputSignal > maxim:
            maxim = inputSignal

    print(maxim)




part1()

def part2():
    perm = permutations([5, 6, 7, 8, 9])
    maxim = 0
    for p in perm:
        amps = [Amplifier(list(prog), i) for i in p]
        for i in range(5):
            amps[i].Next = amps[(i + 1) % 5]
        
        inputSignal = 0
        curr = 0
        while amps[4].running:
            amps[curr].AddInputSignal(inputSignal)
            amps[curr].excute()
            inputSignal = amps[curr].OutputSignal
            curr = (curr + 1) % 5
        
        maxim = max(maxim, amps[4].OutputSignal)

    print(maxim)
part2()

