# part 1

floor = 0

with open("2015-12-01_input.txt") as input:
    for line in input.readlines():
        for instruction in line:
            if instruction == "(":
                floor += 1
            if instruction == ")":
                floor -= 1
print(f"floor: {floor}")