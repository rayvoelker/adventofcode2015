floor = 0
instruction_count = 0

with open("2015-12-01_input.txt") as input:
    for line in input.readlines():
        for instruction in line:
            instruction_count += 1
            if instruction == "(":
                floor += 1
            if instruction == ")":
                floor -= 1
                if floor == -1:
                    print(f"-1 at instruction {instruction_count}")
                    break
