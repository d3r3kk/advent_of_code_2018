import collections
import os


def read_input_file(file_path):
    """Read in a text file containing post-fix integers."""

    input_values = []
    with open(file_path, "r") as input_file:
        input_values = [line.rstrip() for line in input_file]

    return input_values


def input_file(file_name="input.txt"):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, file_name)


def get_frequencies(input_list):
    """
    Return the number of times a character appears in a line.

    Only if a specific character appears twice, or three times.
    """
    two_counts = 0
    three_counts = 0

    for line in input_list:
        counter = collections.Counter(list(line))
        two_occurances = {k: v for k, v in counter.items() if v == 2}
        three_occurances = {k: v for k, v in counter.items() if v == 3}

        if len(two_occurances) > 0:
            two_counts += 1
        if len(three_occurances) > 0:
            three_counts += 1

    return two_counts, three_counts


def get_checksum(file_path):
    input_list = read_input_file(input_file(file_path))
    twos, threes = get_frequencies(input_list)

    return twos * threes


def duplicated_split(line, removal_index):
    if removal_index == len(line) - 1:
        return line
    elif removal_index < 0 or removal_index >= len(line):
        raise IndexError("You are out of the range of the input line.")

    return line[:removal_index], line[removal_index + 1 :]  # noqa


def get_samesies(file_path):
    input_list = read_input_file(input_file(file_path))
    max_removal_index = len(input_list[0]) - 1
    removal_index = 0

    while max_removal_index >= removal_index:
        newlist = []
        for line in input_list:
            leftside, rightside = duplicated_split(line, removal_index)
            newlist.append(leftside + rightside)
        counter = collections.Counter(newlist)
        for box_label, count in counter.items():
            if count == 2:
                return box_label

        removal_index += 1

    return "NO SOLUTION TRY AGAIN"


if __name__ == "__main__":
    day_2_puzzle_1 = get_checksum("input_file.txt")
    print(f"Checksum for box IDs is {day_2_puzzle_1}.")

    day_2_puzzle_2 = get_samesies("input_file.txt")
    print(f"Answer for Day 2 Puzzle 2 {day_2_puzzle_2}.")
