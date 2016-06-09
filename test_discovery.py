"""
pytest looks for tests according to naming conventions,
not whether something is a sub-class of unittest.TestCase.
Tests can be functions or methods on classes.

pytest's test discovery rules are described here:
http://pytest.org/latest/goodpractices.html#test-discovery

The discovery rules are also customizable:
http://pytest.org/latest/example/pythoncollection.html#changing-naming-conventions

Command:

py.test -v test_discovery.py

"""

def test_function():
    assert 42 == 42


class TestClass:
    def test_method1(self):
        assert True

    def test_method2(self):
        x = 1
        y = 2
        assert x == y
