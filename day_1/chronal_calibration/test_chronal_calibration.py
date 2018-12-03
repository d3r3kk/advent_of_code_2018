import chronal_calibration


def test_input():
    return chronal_calibration.input_file("test_input.txt")


def test_input_file():
    input_vals = chronal_calibration.read_input(test_input())

    assert input_vals is not None


def test_input_file_content_positive_values():
    input_vals = chronal_calibration.read_input(test_input())

    assert input_vals[0] == 1


def test_input_file_content_positive_values2():
    input_vals = chronal_calibration.read_input(test_input())

    assert input_vals[2] == 3


def test_input_file_content_negative_values():
    input_vals = chronal_calibration.read_input(test_input())

    assert input_vals[1] == -2


def test_input_file_content_negative_values2():
    input_vals = chronal_calibration.read_input(test_input())

    assert input_vals[3] == -4


def test_chronal_calibration():
    value = chronal_calibration.recalibrate_device(test_input())

    assert value == -2
