import unittest

from decs.testing import repeat


class RepeatTest(unittest.TestCase):

    def setUp(self):
        self.times = list(range(100))

    def test_times_func_repeated(self):

        for i in self.times:
            class TestTimes:
                def __init__(self):
                    self.count = 0

                @repeat(i)
                def foo(self):
                    self.count += 1

            util_class = TestTimes()
            util_class.foo()

            self.assertEqual(i, util_class.count)
