nums = open('5.in').read().split(',')
prog = []
for num in nums:
    prog.append(int(num))

def part1(prog, IDSys):
    i = 0
    while True:
        opcode     = prog[i] % 100
        param1mode = prog[i] // 100 % 10
        param2mode = prog[i] // 1000 % 10
        param3mode = prog[i] // 10000 % 10
        
        match opcode:
            case 1:
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
                

                idx3 = prog[i + 3]
                prog[idx3] = op1 + op2
                i += 4
            case 2:
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

                idx3 = prog[i + 3]
                prog[idx3] = op1 * op2
                i += 4
            case 3:
                idx1 = prog[i + 1]
                prog[idx1] = IDSys
                i += 2
            case 4:
                if param1mode == 0: 
                    idx1 = prog[i + 1]
                    op1 = prog[idx1]
                else:
                    op1 = prog[i + 1]
                
                print(op1)
                i += 2
            case 99:
                break
            case other:
                i += 1
                continue
        
    return prog


#part1
ret = part1(list(prog), 1)

#part2
def part2(prog, IDSys):
    i = 0
    while True:
        opcode     = prog[i] % 100
        param1mode = prog[i] // 100 % 10
        param2mode = prog[i] // 1000 % 10
        param3mode = prog[i] // 10000 % 10
        
        match opcode:
            case 1:
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
                

                idx3 = prog[i + 3]
                prog[idx3] = op1 + op2
                i += 4
            case 2:
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

                idx3 = prog[i + 3]
                prog[idx3] = op1 * op2
                i += 4
            case 3:
                idx1 = prog[i + 1]
                prog[idx1] = IDSys
                i += 2
            case 4:
                if param1mode == 0: 
                    idx1 = prog[i + 1]
                    op1 = prog[idx1]
                else:
                    op1 = prog[i + 1]
                
                print(op1)
                i += 2
            case 5: #jump-if-true
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


                if op1 != 0:
                    i = op2
                    continue
                else:
                    i += 3
            case 6: #jump-if-false
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


                if op1 == 0:
                    i = op2
                    continue
                else:
                    i += 3
            case 7: #less than
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

                idx3 = prog[i + 3]
                if op1 < op2:
                    prog[idx3] = 1
                else:
                    prog[idx3] = 0
                i += 4
            case 8: #equals
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

                idx3 = prog[i + 3]
                if op1 == op2:
                    prog[idx3] = 1
                else:
                    prog[idx3] = 0
                i += 4
            case 99:
                break
            case other:
                i += 1
                continue
        
    return prog

ret = part2(list(prog), 5)

