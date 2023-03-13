from collections import deque
class Amplifier:
    def __init__(self, prog, phasesetting):
        self.prog = prog
        self.i = 0
        self.running = True
        self.PhaseSetting = phasesetting
        self.InputSignal = deque()
        self.InputSignal.append(phasesetting)
        self.Next = None

    def AddInputSignal(self, signal):
        self.InputSignal.append(signal)

    def excute(self):
        if self.running == False:
            print('cannot execute - program halted')
            return
        while True:
            opcode     = self.prog[self.i] % 100
            param1mode = self.prog[self.i] // 100 % 10
            param2mode = self.prog[self.i] // 1000 % 10
            param3mode = self.prog[self.i] // 10000 % 10
            if opcode in [1, 2, 5, 6, 7, 8]:
                if param1mode == 0:
                    idx1 = self.prog[self.i + 1]
                    op1 = self.prog[idx1]
                else:
                    op1 = self.prog[self.i + 1]
                if param2mode == 0:
                    idx2 = self.prog[self.i + 2]
                    op2 = self.prog[idx2]
                else:
                    op2 = self.prog[self.i + 2]

            match opcode:
                case 1:
                    idx3 = self.prog[self.i + 3]
                    self.prog[idx3] = op1 + op2
                    self.i += 4
                case 2:
                    idx3 = self.prog[self.i + 3]
                    self.prog[idx3] = op1 * op2
                    self.i += 4
                case 3:
                    idx1 = self.prog[self.i + 1]
                    self.prog[idx1] = self.InputSignal.popleft()
                    self.i += 2
                case 4:
                    if param1mode == 0: 
                        idx1 = self.prog[self.i + 1]
                        op1 = self.prog[idx1]
                    else:
                        op1 = self.prog[self.i + 1]
                    self.i += 2
                    self.OutputSignal = op1
                    break
                case 5: #jump-if-true
                    if op1 != 0:
                        self.i = op2
                    else:
                        self.i += 3
                case 6: #jump-if-false
                    if op1 == 0:
                        self.i = op2
                    else:
                        self.i += 3
                case 7: #less than
                    idx3 = self.prog[self.i + 3]
                    if op1 < op2:
                        self.prog[idx3] = 1
                    else:
                        self.prog[idx3] = 0
                    self.i += 4
                case 8: #equals
                    idx3 = self.prog[self.i + 3]
                    if op1 == op2:
                        self.prog[idx3] = 1
                    else:
                        self.prog[idx3] = 0
                    self.i += 4
                case 99:
                    self.running = False
                    break
                case _:
                    self.i += 1

    
