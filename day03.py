###########################################################
# Advent of Code 2025 - Day 3
###########################################################
# https://adventofcode.com/2025/day/3
###########################################################
#
#            ____           *                <o             
#   ________/O___\__________|_________________0______   
#      _______||_________                                   
#      | _@__ || _o_    |_ _________________________ 
#      |_&_%__||_oo__^=_[ \|     _    .. .. ..     | 
#                        \_]__--|_|___[]_[]_[]__//_|
#
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)

    total = 0

    for battery in data:
        tens = max(set(battery[:-1]))
        tensIdx = battery.index(str(tens))
        
        ones = max(set(battery[tensIdx + 1:]))

        joltage = int(tens + ones)
        total += joltage

    return total


def test_part1():
    return ['987654321111111', '811111111111119', '234234234234278', '818181911112111']



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part2() # uncomment to run testcase
    # print(data)

    total = 0

    for battery in data:
        joltage = ''
        digits = 12

        for i in range(digits):
            offset = digits - (i + 1)
            offset = -offset if (offset != 0) else 100000000
            
            digit = max(set(battery[:offset]))
            joltage += digit
            
            idx = battery.index(digit)
            battery = battery[idx + 1:]
        
        total += int(joltage)

    return total


def test_part2():
    return ['987654321111111', '811111111111119', '234234234234278', '818181911112111']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day03.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# The initial form of part 2's for in range loop
# (wrote the steps out to wrap my head around the pattern)

        # first = max(set(battery[:-11]))
        # print("options: ", battery[:-11])
        # print(first, type(first))
        # joltage += first
        # firstIdx = battery.index(first)
        # battery = battery[firstIdx + 1:]

        # print("NEW BATTERY: ", battery)

        # first = max(set(battery[:-10]))
        # print(first, type(first))
        # joltage += first
        # firstIdx = battery.index(first)
        # battery = battery[firstIdx + 1:]

        # print("NEW BATTERY: ", battery)

        # first = max(set(battery[:-9]))
        # print(first, type(first))
        # joltage += first
        # firstIdx = battery.index(first)
        # battery = battery[firstIdx + 1:]

        # print("NEW BATTERY: ", battery)

        # first = max(set(battery[:-8]))
        # print(first, type(first))
        # joltage += first
        # firstIdx = battery.index(first)
        # battery = battery[firstIdx + 1:]

        # print("NEW BATTERY: ", battery)

        # first = max(set(battery[:-7]))
        # print(first, type(first))
        # joltage += first
        # firstIdx = battery.index(first)
        # battery = battery[firstIdx + 1:]

        # print("----------------------------------------")
        # print("JOLTAGE: ", joltage)
        # print("----------------------------------------")
