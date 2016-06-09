"""
pytest has a number of builtin fixtures that are useful for testing.
The full list is here:
https://pytest.org/latest/builtin.html#builtin-fixtures-function-arguments

Right now I'm going to focus on tmpdir,
which provides easy access to temporary directories and files for tests:
https://pytest.org/latest/tmpdir.html

By default tmpdir files are not immediately cleaned up,
but you can make fixture that does so.

Commands:

py.test -v -s test_tmpdir.py

"""
import os.path

import pytest


def test_tmpdir(tmpdir):
    print()
    print(tmpdir)
    filepath = tmpdir.mkdir('subdir').join('testfile.txt')
    filepath.write('CONTENTS')

    assert os.path.isfile(str(filepath))


@pytest.yield_fixture
def temp_file(tmpdir):
    filepath = tmpdir.mkdir('subdir').join('testfile.txt')
    filepath.write('CONTENTS')
    yield str(filepath)
    tmpdir.remove()


def test_tmpdir_cleanup(temp_file):
    print()
    print(temp_file)
    assert os.path.isfile(temp_file)
