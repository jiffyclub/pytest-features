"""
pytest provides two ways for fixtures to do teardown.
One is with a finalizer function:
http://pytest.org/latest/fixture.html#fixture-finalization-executing-teardown-code,

and the other is with yield fixtures:
http://pytest.org/latest/yieldfixture.html#yieldfixture

A lot of fixtures provide something to tests so they are injected,
but that's not always necessary:
http://pytest.org/latest/fixture.html#using-fixtures-from-classes-modules-or-projects

Command:

py.test -v -s test_fixture_teardown.py

"""
import pytest


@pytest.fixture
def finalized(request):
    print('\nfixture setup for', request.fixturename)

    def teardown():
        print('\nfixture teardown for', request.fixturename)

    request.addfinalizer(teardown)

    return 'finalized'


@pytest.yield_fixture
def yielder(request):
    print('\nfixture setup for', request.fixturename)
    yield 'yielder'
    print('\nfixture teardown for', request.fixturename)


def test_finalized(finalized):
    assert finalized == 'finalized'


def test_yielder(yielder):
    assert yielder == 'yielder'


@pytest.mark.usefixtures('yielder')
def test_yielder_too():
    pass
