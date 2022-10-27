import typing
import functools

DecoratedFunc = typing.Callable[..., typing.Any]


###############################################################################
# Simple Decorator Template
###############################################################################
def decorator_template(func: DecoratedFunc) -> DecoratedFunc:
    """Template for function decorator without arguments.

    Args:
        func (DecoratedFunc): Function to be decorated.

    Returns:
        DecoratedFunc: Wrapper function decorating decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> typing.Any:
        """Wrapper function called instead of a docorated function.

        It calls decorated function with its original parameters.

        Returns:
            typing.Any: Value returned by decorated function.
        """

        # Actions to be done before calling wrapped function

        ret_val = func(*args, **kwargs)

        # Actions to be done before calling wrapped function

        return ret_val

    return wrapper


###############################################################################
# Decorator with Optional (Keyword) Arguments
###############################################################################
def decorator_with_opt_args(func=None, **dec_kwargs) -> DecoratedFunc:
    """Template for decorator with optional (keyword) arguments.

    Args:
        func:  Function to be decorated or None when there are decorator
               arguments dec_kwargs. Default value: None.
        dec_kwargs: dictionary with optional decorator arguments.

    Returns:
        DecoratedFunc: When called without optional wrapper arguments:
                         returns wrapper function decorating decorated
                         function.
                       When called with wrapper arguments:
                         returns inner decorator responsible for decorating
                         decorated function.
    """

    def inner_decorator(func: DecoratedFunc) -> DecoratedFunc:
        """Template for function decorator without arguments.

        Args:
            func (DecoratedFunc): Function to be decorated.

        Returns:
            DecoratedFunc: Wrapper function decorating decorated function.
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> typing.Any:
            """Wrapper function called instead of docorated function.

            It calls decorated function with its original parameters.

            Returns:
                typing.Any: Value returned by decorated function.
            """

            # Actions to be done before calling wrapped function
            print(F"Inside wrapper with arguments {dec_kwargs!r}")

            ret_val = func(*args, **kwargs)

            # Actions to be done before calling wrapped function

            return ret_val

        print(F"Calling inner_decorator({func!r})")
        return wrapper

    arguments = [F"{func!r}"] + \
                [F"{key}={value!r}" for key, value in dec_kwargs.items()]
    print(F"Calling decorator_with_args({', '.join(arguments)})")
    if func is None and len(dec_kwargs):
        # @decorator(args)  $ with arguments
        return inner_decorator
    elif func is not None and not len(dec_kwargs):
        # @decorator  $ without arguments
        return inner_decorator(func)
    else:
        raise AttributeError("decorator_with_opt_args() can be called with:\n"
                             "- Only one parameter: decorated function, or \n"
                             "- with only keyword decorator parameters ")


###########################################################################
# Function decorated with decorator
###########################################################################
@decorator_with_opt_args(arg1="ARG1")
def test_function1(param1: typing.Any, param2: typing.Any) -> typing.Any:
    """Function to test decorators

    Args:
        param1 (typing.Any): First parameter
        param2 (typing.Any): Second parameter

    Returns:
        typing.Any: Second parameter converted to set
    """
    print(F"Wewnątrz test_function1 {param1!r} {param2!r}")
    return param2


@decorator_with_opt_args
def test_function2(param1: typing.Any, param2: typing.Any) -> typing.Any:
    """Function to test decorators

    Args:
        param1 (typing.Any): First parameter
        param2 (typing.Any): Second parameter

    Returns:
        typing.Any: Second parameter converted to set
    """
    print(F"Wewnątrz test_function2 {param1!r} {param2!r}")
    return param2


def test_function3(param1: typing.Any, param2: typing.Any) -> typing.Any:
    """Function to test decorators

    Args:
        param1 (typing.Any): First parameter
        param2 (typing.Any): Second parameter

    Returns:
        typing.Any: Second parameter converted to set
    """
    print(F"Wewnątrz test_function3 {param1!r} {param2!r}")
    return param2


###############################################################################
# Simple manual tests of decorator with optional arguments
###############################################################################
def main():
    global test_function3

    print(30*"=")

    print("Dekorator z argumentem zaaplikowany do definicji funkcji.")
    print(test_function1(100, 200))
    print(30*"=")

    print("Dekorator bez argumentów zaaplikowany do definicji funkcji.")
    print(test_function2("100", "200"))
    print(30*"=")

    print("Dekorator z argumentem zaaplikowany manualnie.")
    test_function3 = decorator_with_opt_args(arg1="ARGUMENT")(test_function3)
    print(30*"-")
    print(test_function3(100, 200))
    print(30*"=")

    print("Dekorator bez argumentu zaaplikowany manualnie.")
    test_function3 = decorator_with_opt_args(test_function3)
    print(30*"-")
    print(test_function3(100, 200))
    print(30*"=")

    print("Niewłaściwe użycie dekoratora. Wyrzuca wyjątek AttributeError.")
    test_function3 = decorator_with_opt_args(test_function3, arg1="ARGUMENT")
    print(30*"-")
    print(test_function3(100, 200))
    print(30*"=")


if __name__ == "__main__":
    main()
