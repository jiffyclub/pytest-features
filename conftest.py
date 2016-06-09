"""
Fixtures here in the conftest.py file are made available to all the tests
in this directory, and if there were any tests in a directory below here
they would be available to those tests as well.

"""
import pytest


@pytest.fixture(scope='session')
def perm_fixture():
    return 'perm_fixture'
