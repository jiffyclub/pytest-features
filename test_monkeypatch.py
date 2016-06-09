"""
pytest has a number of builtin fixtures that are useful for testing.
The full list is here:
https://pytest.org/latest/builtin.html#builtin-fixtures-function-arguments

Right now I'm going to focus on monkeypatch,
which provides lightweight patching and mocking:
https://pytest.org/latest/monkeypatch.html

Commands:

py.test -v test_monkeypatch.py

"""
import os

import pytest

GLOBAL_DICT = {
    'answer': 42
}


class Pants:
    def ret_pants(self):
        return 'pants'


@pytest.fixture
def pants():
    return Pants()


def setup_module(_):
    os.environ['a_really_great_var'] = 'great'


def teardown_module(_):
    del os.environ['a_really_great_var']


def test_monkeypatch(monkeypatch, pants):
    monkeypatch.setitem(GLOBAL_DICT, 'answer', 54)
    monkeypatch.setenv('a_really_great_var', 'awesome')
    monkeypatch.setattr(Pants, 'ret_pants', lambda _: 'shorts')

    assert GLOBAL_DICT['answer'] == 54
    assert os.environ['a_really_great_var'] == 'awesome'
    assert pants.ret_pants() == 'shorts'


def test_no_monkeypatch(pants):
    assert GLOBAL_DICT['answer'] == 42
    assert os.environ['a_really_great_var'] == 'great'
    assert pants.ret_pants() == 'pants'
