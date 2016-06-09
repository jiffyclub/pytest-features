"""
pytest gives you great failure messages when you use plain assert
statements, even for complex types:
http://pytest.org/latest/assert.html#assert-with-the-assert-statement

pytest's failure messages include helpful things like the value of variables
and verbose stack traces.

Command:

py.test -v test_asserts.py

"""
import math


def test_float():
    assert 3.14159 == math.pi


def test_list():
    assert [1, 2, 3, 4, 5] == [1, 2, 9, 4, 5, 6]


def test_dict():
    assert {'a': 1, 'b': 2, 'c': 3} == \
        {'a': 9, 'b': 2, 'c': 10, 'd': 4}
