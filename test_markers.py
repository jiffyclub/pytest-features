"""
Markers are a way to arbitrarily mark tests so that you can
easily select or de-select certain ones:
http://pytest.org/latest/example/markers.html

Commands:

py.test -v test_markers.py
py.test -v -m 'slow' test_markers.py
py.test -v -m 'not slow' test_markers.py
py.test -v -m 'not slow and not online' test_markers.py
py.test -v -m 'online or postgres' test_markers.py

"""
import pytest


@pytest.mark.slow
def test_something_slow():
    pass


@pytest.mark.online
def test_something_online():
    pass


@pytest.mark.postgres
def test_something_postgres():
    pass
