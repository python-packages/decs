import unittest
import numpy as np

from decs.verification import accepts, returns


class AcceptsTest(unittest.TestCase):
    def setUp(self):
        self.wrong_type_args = \
            [True, str, 1, [1, 2], ['1', '2'], (1, 2), ('1', '2'), {1: 2}, {'1': '2'}, {1, 2}, {'1', '2'}]

        self.right_type_args = ['foo', '1', 'True', 'str']
        self.np_strings = np.array(['foo', '1', 'True', 'str'])

    def tearDown(self):
        del self.wrong_type_args, self.right_type_args

    def test_args_wrong_type_rises_exception(self):
        for arg in self.wrong_type_args:
            self.assertRaises(AssertionError, self.foo, arg)

    def test_args_right_type_no_exception(self):
        for arg in self.right_type_args:
            try:
                self.foo(arg)
            except AssertionError:
                self.fail('This argument value should not lead to an exception')

    def test_args_str_and_np_str_are_interchangeable(self):
        for arg in self.np_strings:
            try:
                self.foo(arg)
            except AssertionError:
                self.fail('str and np.str_ must be interchangeable!')

            self.assertRaises(AssertionError, self.bar, arg)

    def test_kwargs_wrong_type_rises_exception(self):
        wrong_type_kwargs = [{'a': val} for val in self.wrong_type_args]

        for kwargs in wrong_type_kwargs:
            with self.assertRaises(AssertionError):
                self.foo(**kwargs)

    def test_kwargs_right_type_no_exception(self):
        right_type_kwargs = [{'a': val} for val in self.right_type_args]

        for kwargs in right_type_kwargs:
            try:
                self.foo(**kwargs)
            except AssertionError:
                self.fail('This argument value should not lead to an exception')

    def test_kwargs_str_and_np_str_are_interchangable(self):
        kwargs_with_np_strings = [{'a': val} for val in self.np_strings]

        for kwargs in kwargs_with_np_strings:
            try:
                self.foo(**kwargs)
            except AssertionError:
                self.fail('str and np.str_ must be interchangeable!')

            with self.assertRaises(AssertionError):
                self.bar(**kwargs)

    @staticmethod
    @accepts(str)
    def foo(a):
        pass

    @staticmethod
    @accepts(int)
    def bar(a):
        pass


class ReturnsTest(unittest.TestCase):
    def test_wrong_type_rises_exception(self):

        @returns(str)
        def foo():
            return None

        @returns(int)
        def bar():
            return '1'

        self.assertRaises(AssertionError, foo)
        self.assertRaises(AssertionError, bar)

    def test_right_type_no_exception(self):

        @returns(tuple)
        def foo():
            return '1', '2'

        @returns(list)
        def bar():
            return list(range(10))

        try:
            foo()
            bar()
        except AssertionError:
            self.fail('This return value should not lead to an exception')
