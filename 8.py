input = open('8.in').read().strip()

cols = 25
rows = 6



def countDigits(input, n, cols, rows):
    zeros, ones, twos = (0, 0, 0)
    for c in input[n*cols*rows:n*cols*rows + rows*cols]:
        if c == '0':
            zeros += 1
        elif c == '1':
            ones += 1
        elif c == '2':
            twos += 1
    return (zeros, ones, twos)

def p1():
    n = len(input) // (cols * rows)
    minim = 150
    part1 = 0
    for i in range(n):
        zeros, ones, twos = countDigits(input, i, cols, rows)
        if zeros < minim:
            minim = zeros
            part1 = ones * twos
    print(part1)

def p2():
    image = [[[] for _ in range(cols)] for _ in range(rows)]
    size = rows * cols
    layers = len(input) // size

    for k in range(layers):
        for i in range(rows):
            for j in range(cols):
                image[i][j].append(input[k * size + i * cols + j])
    

    for i in range(rows):
        for j in range(cols):
            k = 0
            while image[i][j][k] == '2':
                k += 1
            if image[i][j][k] == '1':
                print('O', sep=None, end='')
            else:
                print(' ', sep=None, end='')
        print()
    

p1()
p2()

pass