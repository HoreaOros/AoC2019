lines = open('6.in').read().strip().split()
A = dict()
B = dict()

for line in lines:
    tokens = line.split(')')
    key = tokens[0]
    value = tokens[1]
    if key in A:
        A[key].append(value)
    else:
        A[key] = [value]

    B[value] = key

def part1(B):
    orbits = 0
    for k in B:
        i = k
        cnt = 1
        while B[i] != 'COM':
            i = B[i]
            cnt += 1
        orbits += cnt

    return orbits

print(part1(B))


def part2(B):
    you = []
    k = 'YOU'
    while k != 'COM':
        you.append(B[k])
        k = B[k]
    
    k = 'SAN'
    cnt = 0
    while not B[k] in you:
        k = B[k]
        cnt += 1
    
    print(cnt + you.index(B[k]) )
    pass
part2(B)