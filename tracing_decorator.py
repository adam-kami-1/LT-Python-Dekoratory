import typing
import functools
import inspect
import time


DecoratedFunc = typing.Callable[..., typing.Any]


###############################################################################
# Simple tracing decorator
###############################################################################
def trace_decorator(func: DecoratedFunc) -> DecoratedFunc:
    """Simple tracing decorator showing how decorated function is called.

    Args:
        func (DecoratedFunc): Function to be decorated.

    Returns:
        DecoratedFunc: Wrapper function decorating decorated function.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arguments = [repr(arg) for arg in args] \
            + [F"{key}={value!r}" for key, value in kwargs.items()]
        print(F"{'-'*5} Calling {func.__name__}({', '.join(arguments)})")
        frame = inspect.stack()[1]
        print(F"Called in {frame.filename}:{frame.lineno}", end="")
        if frame.function.startswith("<"):
            print(F" from {frame.function}")
        else:
            print(F" from function {frame.function}()")

        start = time.perf_counter()
        ret_val = func(*args, **kwargs)
        stop = time.perf_counter()
        print(f"Function executed {stop - start:0.4f} seconds")

        print(F"{'-'*5} Function {func.__name__} returned: {ret_val!r}")
        return ret_val

    return wrapper


###############################################################################
# Function decorated with simple tracing decorator
###############################################################################
@trace_decorator
def test_function1(param1: float, param2: typing.Any) -> typing.Any:
    """Function to test decorators

    Args:
        param1 (typing.Any): First parameter
        param2 (typing.Any): Second parameter

    Returns:
        typing.Any: Second parameter converted to set
    """
    print(F"Wewn¹trz test_function1({param1!r}, {param2!r})")
    time.sleep(param1 / 2)
    return set(param2)


###############################################################################
# Simple manual tests of decorators
###############################################################################
def main():
    print(test_function1)
    print(test_function1.__name__)
    help(test_function1)

    # global test_function1
    # test_function1 = trace_decorator(test_function1)

    print(20*"=")
    print(test_function1(1, "PARAM2"))
    print(20*"=")
    print(test_function1(2, (1, 2, 3, 2)))
    print(20*"=")
    print(test_function1(3, param2={1: "A", 2: "B", 3: "C"}))


if __name__ == "__main__":
    main()
