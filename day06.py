###########################################################
# Advent of Code 2025 - Day 6
###########################################################
# https://adventofcode.com/2025/day/6
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
#   _||__/            \_
#   |^@ |
#   |&%;]
#
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)
    
    methods = data[-1].split()

    newData = []
    for nums in data[:-1]:
        newData.append(nums.split())

    answers = []
    for col in range(len(methods)):
        method = methods[col]
        result = 1
        for row in range(len(newData)):
            num = int(newData[row][col])
            if method == '+':
                result += num
            if method == '*':
                result *= num
        
        answers.append(result if method == '*' else result - 1)

    answerSum = 0
    for answer in answers:
        answerSum += answer
    
    return answerSum


def test_part1():
    return ['123 328  51 64 ', ' 45 64  387 23 ', '  6 98  215 314', '*   +   *   +  ']



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part2() # uncomment to run testcase
    # print(data)

    width = min(len(row) for row in data)
    
    newData = []
    for col in range(width):
        prob = ""
        for row in range(len(data)):
            prob += str(data[row][col])
        newData.append(prob)

    data = newData

    method = ''
    nums = []
    finalAnswer = 0
    for item in data:
        item = item.strip()
        if item.endswith('+') or item.endswith('*'): 
            # first number in new problem
            method = item[-1]
            num = int(item[:-1].strip())
            nums = [num]
        elif item == '':
            # problem over, evaluate and reset
            finalAnswer += evaluateNums(method, nums)
            method = ''
            nums = []

        else:
            nums.append(item)

    finalAnswer += evaluateNums(method, nums)
    return finalAnswer


def evaluateNums(method, nums):
    result = 1
    for num in nums:
        if method == '+':
            result += int(num)
        if method == '*':
            result *= int(num)
    answer = (result - 1 if method == '+' else result)
    return answer


def test_part2():
    return ['123 328  51 64 ', ' 45 64  387 23 ', '  6 98  215 314', '*   +   *   +  ']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.splitlines()]

if __name__ == "__main__":
    with open("inputs/day06.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# 