'''
advent of code day 02
http://adventofcode.com/2017/day/4
'''

with open('inputs/input_day_04', 'r') as f:
    INPUT = f.read()

# Part 1

def count_valid_pass_same(puzzle_input: str) -> int:
    passes = puzzle_input.splitlines()

    total: int = 0

    for passp in passes:
        if len(passp.split(' ')) == len(set(passp.split(' '))):
            total += 1

    return total

# Part 2

def count_valid_pass_anagram(puzzle_input: str) -> int:
    passes = puzzle_input.splitlines()

    total: int = 0

    for passp in passes:
        if (len([''.join(sorted(i)) for i in passp.split(' ')]) ==
                len(set([''.join(sorted(i)) for i in passp.split(' ')]))):
            total += 1

    return total


TEST_INPUT1 = 'aa bb cc dd ee\naa bb cc dd aa\naa bb cc dd aaa'
assert count_valid_pass_same(TEST_INPUT1) == 2

TEST_INPUT2 = 'abcde fghij\nabcde xyz ecdab\na ab abc abd abf abj\niiii oiii ooii oooi oooo\noiii ioii iioi iiio\n'
assert count_valid_pass_anagram(TEST_INPUT2) == 3


if __name__ == '__main__':
    print(count_valid_pass_same(INPUT))
    print(count_valid_pass_anagram(INPUT))
