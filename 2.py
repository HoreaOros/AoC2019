nums = open('2.in').read().split(',')
prog = []
for num in nums:
    prog.append(int(num))

def part1(prog, v1, v2):
    prog[1] = v1
    prog[2] = v2

    i = 0
    while True:
        opcode = prog[i]
        idx1 = prog[i + 1]
        idx2 = prog[i + 2] 
        idx3 = prog[i + 3]
        match opcode:
            case 1:
                prog[idx3] = prog[idx1] + prog[idx2]
            case 2:
                prog[idx3] = prog[idx1] * prog[idx2]
            case 99:
                break
            case other:
                i += 1
                continue
        i += 4
    return prog


#part1
ret = part1(list(prog), 12, 2)
print(ret[0])


#part2
found = False
for noun  in range(100):
    for verb in range(100):
        ret = part1(list(prog), noun, verb)
        if ret[0] == 19690720:
            found = True
            break
    if found:
        break

print(100 * noun + verb)





