"""
pytest has a number of builtin fixtures that are useful for testing.
The full list is here:
https://pytest.org/latest/builtin.html#builtin-fixtures-function-arguments

Right now I'm going to focus on capsys,
which allows you to test output to stdout and stderr:
https://pytest.org/latest/capture.html

Commands:

py.test -v test_capsys.py

"""
import sys


def stdout():
    print('hi on stdout')


def stderr():
    sys.stderr.write('hi on stderr')


def test_capsys(capsys):
    stdout()
    stderr()

    out, err = capsys.readouterr()

    assert out == 'hi on stdout\n'
    assert err == 'hi on stderr'
