"""
Fixtures can be placed in separate, specially named conftest.py files,
from which they will be available to any test in or below the directory
in which the conftest.py file sits. A project can contain multiple
conftest.py files; there might be one at the top level for global fixtures,
and some in specific directories to provide fixtures related
to certain functionality:
http://pytest.org/latest/fixture.html#sharing-a-fixture-across-tests-in-a-module-or-class-session

Command:

py.test -v test_fixture_sharing.py

"""

def test_conftest(perm_fixture):
    assert perm_fixture == 'perm_fixture'
