###########################################################
# Advent of Code 2025 - Day 4
###########################################################
# https://adventofcode.com/2025/day/4 
###########################################################
#
#            ____           *                <o             
#   ________/O___\__________|_________________0______   
#      _______||_________                                   
#      | _@__ || _o_    |_ _________________________ 
#      |_&_%__||_oo__^=_[ \|     _    .. .. ..     | 
#                        \_]__--|_|___[]_[]_[]__//_|
#                                  ____________//___
#                                ..| \ '''''' // @@|
#                                ..__[#]_@@__//_@@@|
#
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)

    count = 0

    for rowIdx in range(len(data)):
        row = data[rowIdx]
        for colIdx in range(len(data[0])):
            spot = row[colIdx]
            if spot != '@': 
                continue

            neighbors = getNeighborCount(data, rowIdx, colIdx)
            if neighbors < 4: 
                count += 1

    return count


def getNeighborCount(data, row, col):
    neighborCount = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dc == 0 and dr == 0:
                continue 
            
            nr, nc = row + dr, col + dc
            if nr not in range(0, len(data)) or nc not in range(0, len(data[0])):
                continue
 
            if data[nr][nc] == '@':
                neighborCount += 1

    return neighborCount


def test_part1():
    return ['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.']



###########################################################
# PART 2

def solve_part2(data):
    # print(data)
    # data = test_part2() # uncomment to run testcase
    
    count = 0
    while True:
        removed, newData = removeRolls(data)

        if removed == 0:
            return count

        data = newData
        count += removed


def removeRolls(data):
    # print(data)
    count = 0
    newData = []

    for rowIdx in range(len(data)):
        row = data[rowIdx]
        newRow = ''
        for colIdx in range(len(data[0])):
            spot = row[colIdx]
            if spot != '@': 
                newRow = newRow + spot
                continue

            neighbors = getNeighborCount(data, rowIdx, colIdx)
            if neighbors < 4: 
                count += 1
                newRow = newRow + '.'
            else:
                newRow = newRow + '@'

        newData.append(newRow)

    return (count, newData)


def test_part2():
    return ['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day04.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# 