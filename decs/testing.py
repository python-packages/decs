import functools


def repeat(times):
    """
    Decorated function will be executed `times` times.

    Warnings:
        Can be applied only for function with no return value.

    Args:
        times(int): required number of times for the function to be repeated.

    Returns:
        (None)
    """

    def repeat_helper(func):
        @functools.wraps(func)
        def call_helper(*args):
            for i in range(times):
                func(*args)

        return call_helper

    return repeat_helper
