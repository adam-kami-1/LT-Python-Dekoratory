import typing
import functools


DecoratedFunc = typing.Callable[..., typing.Any]


###############################################################################
# Decorator used to redirect output from print()
###############################################################################
def print_director(func: DecoratedFunc) -> DecoratedFunc:
    """Decorator used to redirect output from print.

    Args:
        func (DecoratedFunc): Function to be decorated. Usually print.

    Returns:
        DecoratedFunc: Wrapper function decorating print.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global target
        func(*args, **kwargs)
        kwargs["file"] = target
        return func(*args, **kwargs)

    return wrapper


def redirect_on():
    global print, target
    print = print_director(print)
    target = open("log.txt", "a")


def redirect_off():
    global print, target
    print = __builtins__.print
    target.close()


def test_function1(param1: typing.Any, param2: typing.Any) -> typing.Any:
    print(F"Wewn¹trz test_function1({param1!r}, {param2!r})")
    return set(param2)


###############################################################################
# Simple manual tests of decorators
###############################################################################
def main():
    redirect_on()
    print(test_function1("param", [1, 2, 3, 2]))
    print(test_function1(500, (1, 2, 3, 2)))
    print(test_function1(900, param2={1: "A", 2: "B", 3: "C"}))
    redirect_off()
    print(test_function1("PARAM", [4, 5, 6, 7]))
    print(test_function1(1000, (4, 5, 6, 7)))
    print(test_function1(2000, param2={4: "D", 5: "E", 6: "F"}))


if __name__ == "__main__":
    main()
