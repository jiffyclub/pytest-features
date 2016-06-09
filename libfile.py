def square(x):
    """A function where we want to pause and inspect things."""
    import pytest; pytest.set_trace()
    return x * 2


def bad_stuff(x):
    """A function where an exception is going to def happen."""
    return x / 0
