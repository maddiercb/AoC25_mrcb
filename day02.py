###########################################################
# Advent of Code 2025 - Day 2
###########################################################
# https://adventofcode.com/2025/day/2
###########################################################
#
#            ____           *                <o             
#   ________/O___\__________|_________________0______  
#      _______||_________                                   
#      | _@__ || _o_    |_ _________________________   
#
###########################################################
# PART 1

def solve_part1(data):
    # print(data)
    # data = test_part1() # uncomment to run testcase
    
    invalids = []

    for idRange in data:
        start, end = idRange.split('-')
        start, end = int(start), int(end)

        for id in range(start, end + 1):
            if isRepeatedDigits(str(id)):
                invalids.append(id)

    total = sum(invalids)
    return total


def isRepeatedDigits(n):
    if len(n) % 2 != 0: return False

    length = len(n) // 2
    part = n[0:length]

    if n == part * 2:
            return True
    
    return False


def test_part1():
    return parse_input("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")



###########################################################
# PART 2

def solve_part2(data):
    # print(data)
    # data = test_part2() # uncomment to run testcase
    
    invalids = []

    for idRange in data:
        start, end = idRange.split('-')
        start, end = int(start), int(end)

        for id in range(start, end + 1):
            if isRepeatedDigits_2(str(id)):
                invalids.append(id)

    total = sum(invalids)
    return total


def test_part2():
    return parse_input("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")


def isRepeatedDigits_2(n):
    for length in range(1, len(n) // 2 + 1):        
        part = n[0:length]
        times = len(n) // length

        if n == part * times:
            return True
    
    return False


###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().split(',')]

if __name__ == "__main__":
    with open("inputs/day02.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# 