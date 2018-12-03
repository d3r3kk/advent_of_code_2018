import collections
import os


def read_input(file_path):
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
    input_list = read_input(input_file(file_path))
    twos, threes = get_frequencies(input_list)

    return twos * threes


def duplicated_split(input_list, removal_index):
    pass


def get_samesies(file_path):
    input_list = read_input(input_file(file_path))
    max_removal_index = len(input_list[0]) - 1
    removal_index = 0

    leftside = None
    while leftside is None and max_removal_index >= removal_index:
        leftside, rightside = duplicated_split(input_list, removal_index)
        removal_index += 1


if __name__ == "__main__":
    day_2_puzzle_1 = get_checksum("input_file.txt")
    print(f"Checksum for box IDs is {day_2_puzzle_1}.")

    day_2_puzzle_2 = get_samesies("input_file.txt")
    print(f"Answer for Day 2 Puzzle 2 {day_2_puzzle_2}.")
