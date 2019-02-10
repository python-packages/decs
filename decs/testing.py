import functools


def repeat(times):
    """
    Decorated function will be executed `times` times.

    Warnings:
        Can be applied only for function with no return value.
        Otherwise the return value will be lost.

    Examples:
        This decorator primary purpose is to repeat execution of some test function multiple times:

        import random

        @repeat(10)
        def test_int_is_taken():
            examples = list(range(10)
            assert type(random.choice(examples)) == int, 'Error!'

        # No error, test is repeated 10 times.

    Args:
        times(int): required number of times for the function to be repeated.

    Returns:
        None
    """

    def repeat_helper(func):

        @functools.wraps(func)
        def call_helper(*args):
            for i in range(times):
                func(*args)

        return call_helper

    return repeat_helper
