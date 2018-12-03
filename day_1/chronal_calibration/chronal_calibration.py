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


def recalibrate_device(file_path=None):
    input = read_input(input_file(file_path))

    return sum(input)


def get_repeating_freq(file_path=None):
    input = read_input(input_file(file_path))

    duplicated_frequency = None
    frequencies = {0}
    freq = 0

    while duplicated_frequency is None:
        for frequency_modifier in input:
            freq = freq + frequency_modifier
            if freq in frequencies:
                duplicated_frequency = freq
                break
            else:
                frequencies.add(freq)

    return duplicated_frequency


if __name__ == "__main__":
    recalibration_frequency = recalibrate_device(input_file())
    print(f"Recalibration frequency is {recalibration_frequency}")

    repeating_frequency = get_repeating_freq(input_file())
    print(f"First repeating frequency is {repeating_frequency}")
