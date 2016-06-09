"""
Tests can be parametrized to turn one chunk of test code into
a multitude of tests:
http://pytest.org/latest/parametrize.html#parametrized-test-functions

pytest will try to construct a name for your test based on the parameters
(so you can tell them apart), but if necesary you can specify your own
names or a callable that returns a name, via the ids argument.

Command:

py.test -v test_parameters.py

"""
import glob
import os.path

import pytest


@pytest.mark.parametrize('test_file', glob.glob('*.py'))
def test_file_exists(test_file):
    assert os.path.exists(test_file)


@pytest.mark.parametrize(
    'a, b', [({'a': 1}, {'b': 2})], ids=lambda x: str(x))
def test_test_names(a, b):
    pass
