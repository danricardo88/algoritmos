# from challenges.challenge_encrypt_message import encrypt_message

from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 'test')

    assert encrypt_message('test', 1) == 't_tse'
    assert encrypt_message('test', 2) == 'ts_et'
    assert encrypt_message("test", 3) == "set_t"
    assert encrypt_message("trybe", 4) == "e_byrt"
    assert encrypt_message('987654321', 0) == '123456789'

    # assert encrypt_message("python", 3) == "tho_nyp"
