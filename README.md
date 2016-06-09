# Intro to pytest Features

The following is a brief rundown of some of [pytest's](https://pytest.org)
features that make writing tests awesome and fun.
In each section there is a link to a file with a demonstration and a
command you can run at the command-line to run the tests.
Sometimes there are multiple commands you can run to illustrate
different parts of the demonstration.
Clone this repo so you can run and modify it yourself!

- [Test Discovery](#test-discovery)
- [Setup and Teardown](#setup-and-teardown)
- [Plain Asserts](#plain-asserts)
- [Parametrized Tests](#parametrized-tests)
- [Fixtures](#fixtures)
- [Sharing Fixtures](#sharing-fixtures)
- [Fixture Teardown](#fixture-teardown)
- [Markers](#markers)
- [Test Selection](#test-selection)
- [Debugging](#debugging)
- [Built-in Utility Fixtures](#built-in-utility-fixtures)

## Test Discovery

pytest looks for tests according to naming conventions,
not whether something is a sub-class of unittest.TestCase.
Tests can be functions or methods on classes.

pytest's test discovery rules are described here:
http://pytest.org/latest/goodpractices.html#test-discovery

The discovery rules are also customizable:
http://pytest.org/latest/example/pythoncollection.html#changing-naming-conventions

File: [test_discovery.py](./test_discovery.py)

Command: `py.test -v test_discovery.py`

## Setup and Teardown

pytest supports setup and teardown in much the same way
as unittest.TestCase, but you can also do it at the module level:
http://pytest.org/latest/xunit_setup.html#xunitsetup

(But, spoiler alert: you don't end up using this much because
pytest's fixture system is so amazing.)

File: [test_setup_teardown.py](./test_setup_teardown.py)

Command: `py.test -v -s test_setup_teardown.py`

## Plain Asserts

pytest gives you great failure messages when you use plain assert
statements, even for complex types:
http://pytest.org/latest/assert.html#assert-with-the-assert-statement

pytest's failure messages include helpful things like the value of variables
and verbose stack traces.

File: [test_asserts.py](./test_asserts.py)

Command: `py.test -v test_asserts.py`

## Parametrized Tests

Tests can be parametrized to turn one chunk of test code into
a multitude of tests:
http://pytest.org/latest/parametrize.html#parametrized-test-functions

pytest will try to construct a name for your test based on the parameters
(so you can tell them apart), but if necesary you can specify your own
names or a callable that returns a name, via the ids argument.

File: [test_parameters.py](./test_parameters.py)

Command: `py.test -v test_parameters.py`

## Fixtures

Fixtures are a way of providing setup, teardown, and test data.
In contrast to the `setup_*` and `teardown_*` utilities we saw earlier,
fixtures can inject data straight into tests, avoiding the need to
attach test fixtures to a test object:
http://pytest.org/latest/fixture.html#fixture

Fixtures can have a scope defined on them so that pytest can avoid
re-running the fixtures for every single test if that's not
necesary.

In the same way that fixtures can be used as inputs for tests, they
can also be used as inputs for other fixtures:
http://pytest.org/latest/fixture.html#modularity-using-fixtures-from-a-fixture-function

And just like tests can be parametrized, so can fixtures:
http://pytest.org/latest/fixture.html#parametrizing-a-fixture

File: [test_fixtures.py](./test_fixtures.py)

Command: `py.test -v test_fixtures.py`

## Sharing Fixtures

Fixtures can be placed in separate, specially named conftest.py files,
from which they will be available to any test in or below the directory
in which the conftest.py file sits. A project can contain multiple
conftest.py files; there might be one at the top level for global fixtures,
and some in specific directories to provide fixtures related
to certain functionality:
http://pytest.org/latest/fixture.html#sharing-a-fixture-across-tests-in-a-module-or-class-session

Files:

- [test_fixture_sharing.py](./test_fixture_sharing.py)
- [conftest.py](./conftest.py)

Command: `py.test -v test_fixture_sharing.py`

## Fixture Teardown

pytest provides two ways for fixtures to do teardown.
One is with a finalizer function:
http://pytest.org/latest/fixture.html#fixture-finalization-executing-teardown-code,

and the other is with yield fixtures:
http://pytest.org/latest/yieldfixture.html#yieldfixture

A lot of fixtures provide something to tests so they are injected,
but that's not always necessary so you can declare fixture usage from a
decorator:
http://pytest.org/latest/fixture.html#using-fixtures-from-classes-modules-or-projects

File: [test_fixture_teardown.py](./test_fixture_teardown.py)

Command: `py.test -v -s test_fixture_teardown.py`

## Markers

Markers are a way to arbitrarily mark tests so that you can
easily select or de-select certain ones:
http://pytest.org/latest/example/markers.html

File: [test_markers.py](./test_markers.py)

Commands:

- `py.test -v test_markers.py`
- `py.test -v -m 'slow' test_markers.py`
- `py.test -v -m 'not slow' test_markers.py`
- `py.test -v -m 'not slow and not online' test_markers.py`
- `py.test -v -m 'online or postgres' test_markers.py`

## Test Selection

You can select individual tests or groups of tests to run by
three different methods. One is marking:
http://pytest.org/latest/example/markers.html#marking-test-functions-and-selecting-them-for-a-run

Another is by node (exact test name):
http://pytest.org/latest/example/markers.html#selecting-tests-based-on-their-node-id

And finally there is the -k option (string matching on test name):
http://pytest.org/latest/example/markers.html#using-k-expr-to-select-tests-based-on-their-name

File: [test_selection.py](./test_selection.py)

Commands:

- `py.test -v -m 'marked' test_selection.py`
- `py.test -v -m 'not marked' test_selection.py`
- `py.test -v test_selection.py::test_pants`
- `py.test -v test_selection.py::TestThings`
- `py.test -v test_selection.py::TestThings::test_method1`
- `py.test -v -k pants test_selection.py`
- `py.test -v -k 'pants or method' test_selection.py`
- `py.test -v -k 'not pants' test_selection.py`

## Debugging

pytest captures output to stdout and stderr, which can interfere with
debugging tests. If you need to set a break point use the
`pytest.set_trace()` function instead of `pdb.set_trace()`.
To drop into a debugger on test failures use the `--pdb` option to pytest.

Files:

- [test_debugging.py](./test_debugging.py)
- [libfile.py](./libfile.py)

Commands:

- `py.test -v -k square test_debugging.py`
- `py.test -v --pdb -k bad_stuff test_debugging.py`

## Built-in Utility Fixtures

pytest has a number of builtin fixtures that are useful for testing.
The full list is here:
https://pytest.org/latest/builtin.html#builtin-fixtures-function-arguments

Below I'll go into a little more detail on a couple of them.

### monkeypatch

monkeypatch provides lightweight patching and mocking:
https://pytest.org/latest/monkeypatch.html

File: [test_monkeypatch.py](./test_monkeypatch.py)

Command: `py.test -v test_monkeypatch.py`

### tmpdir

tmpdir provides easy access to temporary directories and files for tests:
https://pytest.org/latest/tmpdir.html

By default tmpdir files are not immediately cleaned up,
but you can make fixture that does so.

File: [test_tmpdir.py](./test_tmpdir.py)

Command: `py.test -v -s test_tmpdir.py`

### capsys

capsys allows you to test output to stdout and stderr:
https://pytest.org/latest/capture.html

File: [test_capsys.py](./test_capsys.py)

Command: `py.test -v test_capsys.py`
