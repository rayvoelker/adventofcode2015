total_f = 0
with open("2015-12-02_input.txt") as input:
    # with open("2015-12-02_test_input.txt") as input:
    for line in input.readlines():
        values = list(map(int, line.strip("\n").split("x")))
        # A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon
        # to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for
        # a total of 34 feet.

        # find the smallest perimeter of any one face.
        # 2l + 2w
        # 2l + 2h
        # 2w + 2h
        perimeters = []
        perimeters.append((2 * values[0]) + (2 * values[1]))
        perimeters.append((2 * values[0]) + (2 * values[2]))
        perimeters.append((2 * values[1]) + (2 * values[2]))
        perimeters.sort()

        feet = perimeters[0] + (values[0] * values[1] * values[2])

        print(f"feet:{feet}")

        total_f = total_f + feet

        print()

print(f"total feet of ribbon needed: {total_f}")
#   3783758
