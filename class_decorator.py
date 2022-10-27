def add_repr(cls):

    def repr(self):
        val = []
        for attr in dir(self):
            if not attr.startswith("_"):
                val.append(F"{attr}={getattr(self, attr)!r}")
        return self.__class__.__qualname__ + "(" + ", ".join(val) + ")"

    # if not hasattr(cls, "__repr__"):
    setattr(cls, "__repr__", repr)
    return cls


@add_repr
class MyClass:

    def __init__(self, a: int, b: str):
        self.a = a
        self.b = b


def main():
    obj = MyClass(1, "a")
    print(obj)
    print(repr(obj))
    print(str(obj))


if __name__ == "__main__":
    main()
