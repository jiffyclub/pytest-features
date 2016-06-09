"""
Fixtures are a way of providing setup, teardown, and test data.
In contrast to the setup_* and teardown_* utilities we saw earlier,
fixtures can inject data straight into tests, avoiding the need to
attach test fixtures to a test object:
http://pytest.org/latest/fixture.html#fixture

Fixtures can have a scope defined on them so that pytest can avoid
re-running the fixtures for every single test if that's not
necesary.

In the same way that fixtures can be used as inputs for tests, they
can also be used as inputs for other fixtures:
http://pytest.org/latest/fixture.html#modularity-using-fixtures-from-a-fixture-function

And just like tests can be parametrized, so can fixtures:
http://pytest.org/latest/fixture.html#parametrizing-a-fixture

Command:

py.test -v test_fixtures.py

"""
import glob
import os.path

import pytest


@pytest.fixture
def num():
    return 42


@pytest.fixture
def str_num_squared(num):
    return str(num ** 2)


@pytest.fixture(
    scope='module',
    params=glob.glob('*.py'))
def py_file(request):
    return os.path.abspath(request.param)


def test_num(num):
    assert num == 42


def test_str_num(str_num_squared):
    assert str_num_squared == '1764'


def test_py_file(py_file):
    assert os.path.exists(py_file)
