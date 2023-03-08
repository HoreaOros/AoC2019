infile = open('3.in')

def getProg():
    line = infile.readline().strip()
    prog = line.split(',')
    p = []
    for t in prog:
        p.append((t[0], int(t[1:])))
    return p

p1 = getProg()
p2 = getProg()


def getPath(prog):
    path = []
    x = 0
    y = 0
    for i in prog:
        d, count = i
        for _ in range(count):
            if d == 'R':
                x += 1
            elif d == 'L':
                x -= 1
            elif d == 'U':
                y += 1
            elif d == 'D':
                y -= 1
            path.append((x, y))
    return path




def part1(path1, path2):
    comon = path1.intersection(path2)
    res = min(comon, key = lambda x: abs(x[0]) + abs(x[1]))
    print(abs(res[0]) + abs(res[1]))


def part2(path1, path2):
    comon = set(path1).intersection(set(path2))
    minim = 1000000000
    for p in comon:
        i = path1.index(p)
        j = path2.index(p)
        if i + j + 2 < minim:
            minim = i + j + 2

    print(minim)

path1 = getPath(p1)
path2 = getPath(p2)
part1(set(path1), set(path2))
part2(path1, path2)
