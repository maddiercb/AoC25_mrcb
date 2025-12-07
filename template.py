###########################################################
# Advent of Code 2025 - Day #
###########################################################
# https://adventofcode.com/2025/day/#
###########################################################
#
#            ____           *                               
#   ________/O___\__________|________________________  
#   ADD MORE TREE!
#
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    print(data)


def test_part1():
    return []



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part2() # uncomment to run testcase
    print(data)


def test_part2():
    return []



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day##.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    # print("Part 2:", solve_part2(data))



###########################################################
# 