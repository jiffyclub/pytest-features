"""
You can select individual tests or groups of tests to run by
three different methods. One is marking:
http://pytest.org/latest/example/markers.html#marking-test-functions-and-selecting-them-for-a-run

Another is by node (exact test name):
http://pytest.org/latest/example/markers.html#selecting-tests-based-on-their-node-id

And finally there is the -k option (string matching on test name):
http://pytest.org/latest/example/markers.html#using-k-expr-to-select-tests-based-on-their-name

Commands:

py.test -v -m 'marked' test_selection.py
py.test -v -m 'not marked' test_selection.py
py.test -v test_selection.py::test_pants
py.test -v test_selection.py::TestThings
py.test -v test_selection.py::TestThings::test_method1
py.test -v -k pants test_selection.py
py.test -v -k 'pants or method' test_selection.py
py.test -v -k 'not pants' test_selection.py

"""
import pytest


@pytest.mark.marked
def test_marked():
    pass


class TestThings:
    def test_method1(self):
        pass

    def test_method2(self):
        pass


def test_pants():
    pass
