

class ExampleClass:

    _priv_class_attr: int = 100

    def __init__(self, param: int):
        self._private_attr = param

    @staticmethod
    def get_ca() -> int:
        return ExampleClass._priv_class_attr

    @staticmethod
    def set_ca(value: int):
        ExampleClass._priv_class_attr = value

    @property
    def attr(self) -> int:
        return self._private_attr

    @attr.setter
    def attr(self, value: int):
        self._private_attr = value


def use_example_class():

    print("Dwie przykładowe instancje klasy ExampleClass")
    example1 = ExampleClass(5)
    example2 = ExampleClass(10)

    print("'Nielegalny' dostęp do prywatnych globalnych atrybutów klasy")
    print(ExampleClass._priv_class_attr)
    print(example1._priv_class_attr)
    ExampleClass._priv_class_attr = 200

    print("Użycie statycznej metody")
    print(ExampleClass.get_ca())
    print(example1.get_ca())
    print(example2.get_ca())

    ExampleClass.set_ca(300)
    print(example1.get_ca())

    print("'Nielegalny' dostęp do prywatnych atrybutów instancji klasy")
    print(example1._private_attr)
    print(example2._private_attr)

    print("Użycie gettera")
    print(example1.attr)
    print(example2.attr)

    print("Użycie settera")
    example1.attr = 8
    print(example1.attr)
    example2.attr = 16
    print(example2.attr)


if __name__ == "__main__":
    use_example_class()
