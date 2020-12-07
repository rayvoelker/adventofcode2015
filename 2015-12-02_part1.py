total_sq_f = 0
with open("2015-12-02_input.txt") as input:
    # with open("2015-12-02_test_input.txt") as input:
    for line in input.readlines():
        values = list(map(int, line.strip("\n").split("x")))
        # 2*l*w + 2*w*h + 2*h*l
        sides = []
        sides.append(values[0] * values[1])
        sides.append(values[1] * values[2])
        sides.append(values[0] * values[2])
        sides.sort()

        sq_f = sum(list(map(lambda x: x * 2, sides))) + sides[0]

        total_sq_f = total_sq_f + sq_f
        print()

print(f"total square feet needed: {total_sq_f}")
