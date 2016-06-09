"""
pytest supports setup and teardown in much the same way
as unittest.TestCase, but you can also do it at the module level:
http://pytest.org/latest/xunit_setup.html#xunitsetup

(But, spoiler alert: you don't end up using this much because
pytest's fixture system is so amazing.)

Command:

py.test -v -s test_setup_teardown.py

"""

def setup_module(module):
    print('\nsetting up module')
    module.module_var = 'module'


def teardown_module(module):
    print('tearing down module')


class TestSetup:
    @classmethod
    def setup_class(cls):
        print('setting up class', cls.__name__)
        cls.class_var = 'class'

    @classmethod
    def teardown_class(cls):
        print('tearing down class', cls.__name__)

    def setup_method(self, method):
        print('\nsetting up method', method.__name__)

    def teardown_method(self, method):
        print('\ntearing down method', method.__name__)

    def test_module_var(self):
        assert module_var == 'module'

    def test_class_var(self):
        assert self.class_var == 'class'
