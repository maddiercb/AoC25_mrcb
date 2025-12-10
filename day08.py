###########################################################
# Advent of Code 2025 - Day 8
###########################################################
# https://adventofcode.com/2025/day/8
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
#    ||   ____________    _______________________
#   _||__/'...' '...' \_  |.     |~    .''.    .|
#   |^@ |   1  2  3 () |  | '..'/ \'..'    '..' |
#   |&%;]__[]_[]_[]__<>|  |    |H_/|\   \\\\\\  |
#                     '...|<>__|H__|_\__|_____|_[
#
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)

    distancePairs = [] # (distance, p1, p2)
    for p1 in range(len(data) - 1):
        for p2 in range(p1 + 1, len(data)):
            dist = distance_3d(data[p1], data[p2])
            distancePairs.append((dist, data[p1], data[p2]))
    distancePairs.sort()

    ufDict = dict()
    for point in data:
        ufDict[point] = {point}

    comboTarget = 1000
    pairIdx = 0

    while pairIdx < comboTarget:
        dist, p1, p2 = distancePairs[pairIdx]

        p1Root = getRoot(ufDict, p1)
        p2Root = getRoot(ufDict, p2)
        p1Circuit = ufDict[p1Root]
        p2Circuit = ufDict[p2Root]

        # make p1 the larger of the two points
        if len(p2Circuit) > len(p1Circuit):
            p1, p2 = p2, p1
            p1Circuit, p2Circuit = p2Circuit, p1Circuit
            p1Root, p2Root = p2Root, p1Root  

        # check if they're already connected
        if p1Root == p2Root:
            pairIdx += 1
            continue

        # if not already connected, merge circuits
        combinedCircuit = p1Circuit | p2Circuit
        ufDict[p1Root] = combinedCircuit

        for node in p2Circuit:
            ufDict[node] = p1Root

        ufDict[p2Root] = p1Root
        pairIdx += 1

    circuitSizes = sorted([len(val) for val in ufDict.values() if isinstance(val, set)])[::-1]
    return circuitSizes[0] * circuitSizes[1] * circuitSizes[2]


def getRoot(ufDict, box):
    while type(ufDict[box]) != set:
        box = ufDict[box]
    return box


def distance_3d(p1, p2):
    p1 = [int(val) for val in p1.split(',')]
    p2 = [int(val) for val in p2.split(',')]

    x = (p2[0]-p1[0]) ** 2
    y = (p2[1]-p1[1]) ** 2
    z = (p2[2]-p1[2]) ** 2

    return (x + y + z) ** 0.5


def test_part1():
    return ['162,817,812', 
            '57,618,57', 
            '906,360,560', 
            '592,479,940', 
            '352,342,300', 
            '466,668,158', 
            '542,29,236', 
            '431,825,988', 
            '739,650,466', 
            '52,470,668', 
            '216,146,977', 
            '819,987,18', 
            '117,168,530', 
            '805,96,715', 
            '346,949,466', 
            '970,615,88', 
            '941,993,340', 
            '862,61,35', 
            '984,92,344', 
            '425,690,689']



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)

    distancePairs = [] # (distance, p1, p2)
    for p1 in range(len(data) - 1):
        for p2 in range(p1 + 1, len(data)):
            dist = distance_3d(data[p1], data[p2])
            distancePairs.append((dist, data[p1], data[p2]))
    distancePairs.sort()

    ufDict = dict()
    for point in data:
        ufDict[point] = {point}

    pairIdx = 0

    while True:
        dist, p1, p2 = distancePairs[pairIdx]

        p1Root = getRoot(ufDict, p1)
        p2Root = getRoot(ufDict, p2)
        p1Circuit = ufDict[p1Root]
        p2Circuit = ufDict[p2Root]

        # make p1 the larger of the two points
        if len(p2Circuit) > len(p1Circuit):
            p1, p2 = p2, p1
            p1Circuit, p2Circuit = p2Circuit, p1Circuit
            p1Root, p2Root = p2Root, p1Root  

        # check if they're already connected
        if p1Root == p2Root:
            pairIdx += 1
            continue

        # if not already connected, merge circuits
        combinedCircuit = p1Circuit | p2Circuit
        ufDict[p1Root] = combinedCircuit

        for node in p2Circuit:
            ufDict[node] = p1Root

        ufDict[p2Root] = p1Root
        pairIdx += 1

        roots = [v for v in ufDict.values() if isinstance(v, set)]
        if len(roots) == 1:
            break

    p1X, p2X = int(p1.split(',')[0]), int(p2.split(',')[0])
    return p1X * p2X


def test_part2():
    return ['162,817,812', 
            '57,618,57', 
            '906,360,560', 
            '592,479,940', 
            '352,342,300', 
            '466,668,158', 
            '542,29,236', 
            '431,825,988', 
            '739,650,466', 
            '52,470,668', 
            '216,146,977', 
            '819,987,18', 
            '117,168,530', 
            '805,96,715', 
            '346,949,466', 
            '970,615,88', 
            '941,993,340', 
            '862,61,35', 
            '984,92,344', 
            '425,690,689']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day08.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# 
