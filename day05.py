###########################################################
# Advent of Code 2025 - Day 5
###########################################################
# https://adventofcode.com/2025/day/5
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

    split = data.index('')
    strRangesList = data[:split]
    rangesList = []
    idsList = data[split + 1:]
    
    for idRange in strRangesList:
        minId, maxId = (int(val) for val in idRange.split('-'))
        rangesList.append((minId, maxId))

    freshCount = 0
    for stockedId in idsList:
        for minId, maxId in rangesList:
            if minId <= int(stockedId) <= maxId:
                freshCount += 1
                break

    return freshCount


def test_part1():
    return ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part2() # uncomment to run testcase
    # print(data)

    split = data.index('')
    oldRangesList = data[:split]

    rangesList = []
    for idRange in oldRangesList:
        minId, maxId = (int(val) for val in idRange.split('-'))
        rangesList.append((minId, maxId))

    rangesList.sort()
    mergedRanges = mergeRanges(rangesList)

    count = 0
    for min, max in mergedRanges:
        count += (max - min) + 1

    return count
    

def mergeRanges(oldList):
    newList = []
    prevStart, prevEnd = oldList[0]

    for newStart, newEnd in oldList[1:]:
        if newStart <= prevEnd + 1:
            prevEnd = max(prevEnd, newEnd)
        else:
            newList.append((prevStart, prevEnd))
            prevStart, prevEnd = newStart, newEnd
    
    newList.append((prevStart, prevEnd))
    return newList


def test_part2():
    return ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day05.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# Old code of approaches that weren't fast enough but work
# or are close enough but needed pivots

# def solve_part1(data):
#     # data = test_part1() # uncomment to run testcase
#     # print(data)

#     split = data.index('')
#     rangesList = data[:split] # Ranges of fresh ingredients, inclusive
#     idsList = data[split + 1:]

#     freshIds = set()
    
#     for idRange in rangesList:
#         minId, maxId = (int(val) for val in idRange.split('-'))
#         for id in range(minId, maxId + 1):
#             freshIds.add(id)

#     freshCount = 0
#     for stockedId in idsList:
#         if int(stockedId) in freshIds:
#             freshCount += 1

#     return freshCount


# def solve_part2(data):
#     # doesn't take care of double counted ids
#     # data = test_part2() # uncomment to run testcase
#     # print(data)

#     split = data.index('')
#     rangesList = data[:split] # Ranges of fresh ingredients, inclusive
#     count = 0
    
#     for idRange in rangesList:
#         minId, maxId = (int(val) for val in idRange.split('-'))
#         count += (maxId - minId) + 1
    
#     return count


# def solve_part2(data):
#     # works but too slow, can't blow up ranges i fear
#     # data = test_part2() # uncomment to run testcase
#     # print(data)

#     split = data.index('')
#     rangesList = data[:split] # Ranges of fresh ingredients, inclusive
#     freshIds = set()
#     count = 0

#     print("ranges list: ", len(rangesList), " items")
    
#     for idRange in rangesList:
#         minId, maxId = (int(val) for val in idRange.split('-'))
#         # count += (maxId - minId) + 1
#         for id in range(minId, maxId + 1):
#             freshIds.add(id)
#         count += 1
#         if count % 5 == 0:
#             print(f"ranges done: {count}")
    
#     return len(freshIds)
