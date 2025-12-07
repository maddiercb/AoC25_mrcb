###########################################################
# Advent of Code 2025 - Day 7
###########################################################
# https://adventofcode.com/2025/day/7
###########################################################
#
#            ____           *                <o             
#   ________/O___\__________|_________________0______   
#      _______||_________                                   
#      | _@__ || _o_    |_ _________________________ 
#      |_&_%__||_oo__^=_[ \|     _    .. .. ..     | 
#                        \_]__--|_|___[]_[]_[]__//_|
#                                  ____________//___
#   __________________________  ...| \ '''''' // @@|
#   |_. ___ | .--.  ()   ()  |.' ..__[#]_@@__//_@@@|
#   |_\_|^|_]_|==|_T_T_T_T_T_...'
#    ||   ____________
#   _||__/'...' '...' \_
#   |^@ |   1  2  3 () |
#   |&%;]__[]_[]_[]__<>|
#                     '...
#
###########################################################
from collections import Counter
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)

    beamEnds = set()
    beam = data[0].index("S")
    beamEnds.add(beam)
    splits = set()

    for lineIdx in range(1, len(data)):
        newBeams = []
        for beamCol in beamEnds:
            nextChar = data[lineIdx][beamCol]
            if nextChar == '^':
                newBeams.append(beamCol - 1)
                newBeams.append(beamCol + 1)
                splits.add((lineIdx, beamCol))
            else:
                newBeams.append(beamCol)
        beamEnds = set(newBeams)
    
    return len(splits)


def test_part1():
    return ['.......S.......', 
            '...............', 
            '.......^.......', 
            '...............', 
            '......^.^......', 
            '...............', 
            '.....^.^.^.....', 
            '...............', 
            '....^.^...^....', 
            '...............', 
            '...^.^...^.^...', 
            '...............', 
            '..^...^.....^..', 
            '...............', 
            '.^.^.^.^.^...^.', 
            '...............']



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part2() # uncomment to run testcase
    # print(data)

    timelines = Counter()
    beam = data[0].index("S")
    timelines[beam] = 1

    for lineIdx in range(1, len(data)):
        newTimelines = Counter()
        for beamCol, count in timelines.items():
            nextChar = data[lineIdx][beamCol]
            if nextChar == '^':
                newTimelines[beamCol - 1] += count
                newTimelines[beamCol + 1] += count
            else:
                newTimelines[beamCol] += count
        timelines = newTimelines 
    
    total = sum(timelines.values())
    return total


def test_part2():
    return ['.......S.......', 
            '...............', 
            '.......^.......', 
            '...............', 
            '......^.^......', 
            '...............', 
            '.....^.^.^.....', 
            '...............', 
            '....^.^...^....', 
            '...............', 
            '...^.^...^.^...', 
            '...............', 
            '..^...^.....^..', 
            '...............', 
            '.^.^.^.^.^...^.', 
            '...............']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day07.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# 