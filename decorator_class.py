import typing
import time
import random

DecoratedFunc = typing.Callable[..., typing.Any]


###############################################################################
# Simple Decorator Class without Arguments
###############################################################################
class CountCalls:

    def __init__(self, func: DecoratedFunc):
        # print(F"Decorator instantiation for {func.__name__} is called.")
        self._func = func
        self._num_calls = 0

    def __call__(self, *args, **kwargs):
        self._num_calls += 1
        print(F"{self._num_calls}: ", end="")

        return self._func(*args, **kwargs)

    def __repr__(self):
        return F"Function {self._func.__name__} " + \
               F"was called  {self._num_calls} times."


@CountCalls
def say_hello(name: str):
    print(F"Hello {name}!")


@CountCalls
def say_bye(name: str):
    print(F"By {name}!")


def count_calls_test():
    # global say_hello, say_bye
    # say_hello = CountCalls(say_hello)
    # say_bye = CountCalls(say_bye)

    say_hello("Max")
    say_hello("Max")
    say_hello("Bill")
    say_bye("Bill")
    say_hello("Ann")
    say_bye("Ann")
    say_bye("Max")
    print(say_hello)
    print(say_bye)


###############################################################################
# Decorator Class with Optional (Keyword) Arguments
###############################################################################
class TraceUsage:

    def __init__(self,
                 func: typing.Union[DecoratedFunc, None] = None,
                 count_calls: bool = True,
                 sum_time: bool = False):
        self._count_calls = count_calls
        self._sum_time = sum_time
        self._num_calls = 0
        self._time_sum = 0.0
        self._func = func

    def __call__(self, *args, **kwargs):
        if self._func is None:
            self._func = args[0]
            return self
        self._num_calls += 1
        if self._count_calls:
            print(F"{self._num_calls}: ", end="")
        start = 0.0
        if self._sum_time:
            start = time.perf_counter()

        result = self._func(*args, **kwargs)

        if self._sum_time:
            stop = time.perf_counter()
            self._time_sum += stop - start
            print(F"{6 * ' '} {stop - start:0.4f} seconds.")
        return result

    def __repr__(self):
        if self._func is None:
            return ""
        res = ""
        if self._count_calls:
            res += F"Function {self._func.__name__}() "
            res += F"was called  {self._num_calls} times.\n"
        if self._sum_time:
            res += F"All calls took {self._time_sum:0.4f} seconds. "
            res += F"Mean value {self._time_sum/self._num_calls:0.4f} seconds"
        return res


# @TraceUsage(count_calls=True, sum_time=True)
@TraceUsage
def test_func(name: str):
    time.sleep(2 * random.random())
    print(name)


def trace_usage_test():
    test_func("ABC")
    test_func("DEF")
    test_func("GHI")
    test_func("JKL")
    print(test_func)


def main():
    count_calls_test()
    trace_usage_test()


if __name__ == "__main__":
    main()
