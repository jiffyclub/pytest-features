"""
pytest captures output to stdout and stderr, which can interfere with
debugging tests. If you need to set a break point use the
pytest.set_trace() function instead of pdb.set_trace().
To drop into a debugger on test failures use the --pdb option to pytest.

Commands:

py.test -v -k square test_debugging.py
py.test -v --pdb -k bad_stuff test_debugging.py

"""

import libfile


def test_square():
    assert libfile.square(9) == 81


def test_bad_stuff():
    libfile.bad_stuff(42)
