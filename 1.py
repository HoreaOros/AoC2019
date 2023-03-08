infile =open("1.in")
lines = infile.read().split('\n')

numbers = []
for line in lines:
    numbers.append(int(line))

def part1():
    fuelRequirements = []
    for mass in numbers:
        fuelRequirements.append(mass // 3 - 2)
    print(sum(fuelRequirements))

part1()


def part2():
    fuelRequirements = [0 for _ in numbers]
    for i, mass in enumerate(numbers):
        fuel = mass
        while True:
            fuel = fuel // 3 - 2
            if fuel <= 0:
                break
            else:
                fuelRequirements[i] += fuel
    print(sum(fuelRequirements))
part2()
