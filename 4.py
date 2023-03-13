input = '138307-654504'
tokens = input.split('-')
left = int(tokens[0])
right = int(tokens[1])

def meetPwdCriteria(n):
    b = n % 10
    n //= 10
    c1 = True # increasing 
    c2 = False #same consecutive digit
    while n > 0:
        a = n % 10
        n //= 10
        if a > b:
            c1 = False
            break
        if a == b:
            c2 = True
        b = a
    return c1 and c2
def part1(left, right):
    res = 0
    for n in range(left, right + 1):
        if meetPwdCriteria(n):
            res += 1
    return res

print(part1(left, right))

def meetCriteria2(n):
    ok = False
    s = str(n)
    c = 1
    for i in range(1,len(s)):
        if s[i] == s[i - 1]:
            c += 1
        else:
            if c == 2:
                ok = True
                break
            c = 1
    if not ok and c == 2:
        ok = True
    return ok

def part2(left, right):
    res = 0
    for n in range(left, right + 1):
        if meetPwdCriteria(n) and meetCriteria2(n):
            res += 1
    return res

print(part2(left, right))


