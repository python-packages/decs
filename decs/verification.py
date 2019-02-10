import inspect
import functools


def accepts(*types):
    """
    Checks types of function's arguments.
    Idea is taken from: https://www.python.org/dev/peps/pep-0318/

    Args:
        *types(list/tuple): types of parameters of the function.

    Returns:
        (function): initial function.

    Examples:
        Functions types of one or many args or kwargs can be verified:

        @accepts(str)
        def my_print(string):
            print(string)
            return string

        # if type(string) == str passes else raises AssertionError.


        Class methods types of one or many args or kwargs can be verified:

        @accepts('self', str)
        def my_print_method(self, string):
            print(string)
            return string

        # if type(string) == str passes else raises AssertionError.

    Raises:
        AssertionError: if one or more passed types are not equal to the *args, **kwargs types
            (element-wise comparision).
    """

    def check_accepts(func):
        assert len(types) == len(inspect.signature(func).parameters), \
            f'accept number of arguments not equal with function number of arguments in [{func.__qualname__}]'

        @functools.wraps(func)
        def check_args(*args, **kwargs):
            for (a, t) in zip(args, types):
                # Use 'self' as the first argument in a class methods.
                assert t == 'self' or isinstance(a, t), \
                    f"arg [{a}] of type {type(a)} in [{func.__qualname__}] does not match type {t}"

            for kwarg_key, kwarg_val in kwargs.items():
                # If your PyCharm highlights the line below with red, indicating that there is a problem with
                # parametized generics, it's a known bug reported here:
                # https://youtrack.jetbrains.com/issue/PY-33753
                assert isinstance(kwarg_val, types[list(inspect.signature(func).parameters.keys()).index(kwarg_key)]), \
                    f"kwarg [{kwarg_key}] of type {type(kwarg_val)} does not match type " \
                        f"{types[list(inspect.signature(func).parameters.keys()).index(kwarg_key)]}"

            return func(*args, **kwargs)

        return check_args

    return check_accepts


def returns(rtype):
    """
    Checks types of function's return values.
    Idea is taken from: https://www.python.org/dev/peps/pep-0318/

    Args:
        rtype(type): type of value returned by the function.

    Returns:
        (function): initial funtion.

    Examples:
        Return value of the function can be verified the following way:

        @returns(int)
        def my_function():
            return 42

        # No error

        @returns(int)
        def my_function():
            return '42'

        # AssertionError

        @returns(tuple)
        def my_function():
            return 42, 24

        # No error

    Raises:
        AssertionError: if type of return value is not equal to the type passed to the decorator.
    """

    def wraps(func):
        @functools.wraps(func)
        def check_returns(*args, **kwargs):
            result = func(*args, **kwargs)
            assert isinstance(result, rtype), \
                f"return value {result} of type {type(result)} in [{func.__qualname__}] does not match {rtype}"
            return result

        return check_returns

    return wraps

