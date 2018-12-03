import os


def read_input(file_path):
    """Read in a text file containing post-fix integers."""

    input_values = []
    with open(file_path, "r") as input_file:
        input_values = [int(line) for line in input_file]

    return input_values


def input_file(file_name="input.txt"):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, file_name)


def get_checksum(file_path):
    return "[Not Implemented Yet]"


def get_puzz_2_answer(file_path):
    return "[Not Implemented Yet]"


if __name__ == "__main__":
    day_2_puzzle_1 = get_checksum(input_file())
    print(f"Checksum for box IDs is {day_2_puzzle_1}.")

    day_2_puzzle_2 = get_puzz_2_answer(input_file())
    print(f"Answer for Day 2 Puzzle 2 {day_2_puzzle_2}.")
