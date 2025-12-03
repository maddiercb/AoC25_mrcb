###########################################################
# Advent of Code 2025 - Day 1
###########################################################
# https://adventofcode.com/2025/day/1
###########################################################
#
#            ____           *                <o             
#   ________/O___\__________|_________________0______  
#
###########################################################
# PART 1

def solve_part1(data):
    # data = test_part1() # uncomment to run testcase
    # print(data)

    arrow = 50
    count = 0

    for instruction in data:
        dir = instruction[0]
        value = int(instruction[1:])

        if dir == 'L':
            arrow = (arrow - value) % 100
        elif dir == 'R':
            arrow = (arrow + value) % 100
        if arrow == 0: count += 1

    return count    

def test_part1():
    return ["L68", "L30", 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']



###########################################################
# PART 2

def solve_part2(data):
    # data = test_part2() # uncomment to run testcase
    # print(data)

    arrow = 50
    count = 0

    for instruction in data:
        dir = instruction[0]
        value = int(instruction[1:])

        cycles = 0
        steps = value % 100

        if dir == 'L':
            if steps >= arrow and arrow != 0:
                cycles += 1

            newArrow = (arrow - steps) % 100


        if dir == 'R':
            if steps >= (100 - arrow):
                cycles += 1
            
            newArrow = (arrow + steps) % 100

        # print(f"{arrow} -> {instruction} -> {newArrow} ({value // 100} + {cycles})")
        
        arrow = newArrow
        count += value // 100
        count += cycles

    return count

def test_part2():
    # return ["L50"]
    return ["L68", "L30", 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']



###########################################################
# OUTPUT ANSWERS

def parse_input(raw):
    return [x for x in raw.strip().splitlines()]

if __name__ == "__main__":
    with open("inputs/day01.txt") as f:
        raw = f.read()

    data = parse_input(raw)

    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))



###########################################################
# OTHER TEST CASES FOR PART TWO

    # return ["R49"] # 50 -> R49 -> 99 (0)  - little add
    # return ["R50"] # 50 -> R50 -> 0 (1)  - zero add
    # return ["R51"] # 50 -> R51 -> 1 (1)  - big add

    # return ["L49"] # 50 -> L49 -> 1 (0)  - little sub
    # return ["L50"] # 50 -> L50 -> 0 (1)  - zero sub
    # return ["L51"] # 50 -> L51 -> 99 (1)  - big sub

    # return ["R149"] # 50 -> R49 -> 99 (1)  - little add plus hund
    # return ["R150"] # 50 -> R50 -> 0 (2)  - zero add plus hund
    # return ["R151"] # 50 -> R51 -> 1 (2)  - big add plus hund

    # return ["L149"] # 50 -> L49 -> 1 (1)  - little sub plus hund
    # return ["L150"] # 50 -> L50 -> 0 (2)  - zero sub plus hund
    # return ["L151"] # 50 -> L51 -> 99 (2)  - big sub plus hund

    # return ["L100"] # 50 -> L51 -> 99 (2)  - big sub plus hund
    
    # change arrow to 0 for this one...
    # return ["L50"] # 0 -> L50 -> 50 (0) - left from zero