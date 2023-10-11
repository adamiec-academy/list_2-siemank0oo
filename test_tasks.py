import pytest
from test_data import CENSOR_DATA, ENVELOPE_DATA, IS_PRIME_DATA, IS_DIABOLIC_DATA, CIPHER_DATA, DECIPHER_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


@pytest.mark.parametrize("arg, expected_output", CENSOR_DATA, ids=_data_args(CENSOR_DATA))
def test_task_1_censor(arg, expected_output):
    from task_1 import censor
    assert expected_output == censor(arg)


@pytest.mark.parametrize("arg, expected_output", ENVELOPE_DATA, ids=_data_args(ENVELOPE_DATA))
def test_task_2_envelope(capfd, arg, expected_output):
    with capfd.disabled():
        from task_2 import envelope
    envelope(arg)
    actual_output, _ = capfd.readouterr()
    assert expected_output == actual_output


def test_task_3_inflation():
    file = open("task_3.py", "r", encoding="utf-8")
    assert file.readline().strip() != "# Remove this comment to confirm that this task is done"


@pytest.mark.parametrize("arg, expected_output", IS_PRIME_DATA, ids=_data_args(IS_PRIME_DATA))
def test_task_4_is_prime(arg, expected_output):
    from task_4 import is_prime
    assert expected_output == is_prime(arg)


@pytest.mark.parametrize("arg, expected_output", IS_DIABOLIC_DATA, ids=_data_args(IS_DIABOLIC_DATA))
def test_task_4_is_diabolic(arg, expected_output):
    from task_4 import is_diabolic
    assert expected_output == is_diabolic(arg)


@pytest.mark.parametrize("text, shift, expected_output", CIPHER_DATA, ids=_data_args(CIPHER_DATA))
def test_task_5_cipher(text, shift, expected_output):
    from task_5 import cipher
    assert expected_output == cipher(text, shift)


@pytest.mark.parametrize("text, shift, expected_output", DECIPHER_DATA, ids=_data_args(DECIPHER_DATA))
def test_task_5_decipher(text, shift, expected_output):
    from task_5 import decipher
    assert expected_output == decipher(text, shift)
