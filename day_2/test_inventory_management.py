import inventory_management


def test_input():
    return inventory_management.input_file("test_input.txt")


def test_input2():
    return inventory_management.input_file("test_input_2.txt")


def test_input_file():
    input_vals = inventory_management.read_input(test_input())

    assert input_vals is not None

    input_vals = inventory_management.read_input(test_input2())

    assert input_vals is not None


def test_get_frequencies():
    twos, threes = inventory_management.get_frequencies(["aabcdef"])
    assert twos == 1
    assert threes == 0

    twos, threes = inventory_management.get_frequencies(["aaabcde"])
    assert twos == 0
    assert threes == 1


def test_get_frequencies_dont_count_doubles():
    twos, threes = inventory_management.get_frequencies(["aabcdee"])

    assert twos == 1
    assert threes == 0

    twos, threes = inventory_management.get_frequencies(["aaabccc"])

    assert twos == 0
    assert threes == 1


def test_get_frequencies_with_input():
    input_lines = inventory_management.read_input(test_input())
    twos, threes = inventory_management.get_frequencies(input_lines)

    assert twos == 4
    assert threes == 3


def test_get_checksum_with_input():
    checksum = inventory_management.get_checksum(test_input())

    assert checksum == 12


def test_find_samesies():
    pass
