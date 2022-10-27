import dataclasses


@dataclasses.dataclass
class MyClass:
    parami: int
    paramf: float
    params: str
    paraml: list
    paramt: tuple
    paramd: dict


if __name__ == "__main__":
    obj1 = MyClass(1,
                   3.14,
                   "π",
                   paraml=["koń", "krowa", "koza"],
                   paramd={"привіт": "witam"},
                   paramt=(1, 2, 3, 4))
    print("==================================")
    print("Domyślne formatowanie dataclass'y:")
    print(obj1)
    print("================================")
    print("Dostęp do atrybutów dataclass'y:")
    print(obj1.paramt)
    obj1.paramt = ("A", "B", "C")
    print(obj1.paramt)
    print("==================================")
    print("Porównywanie obiektów dataclass'y:")
    obj2 = MyClass(2, 1.5, "", [], (), {})
    print(F"{obj1} is{' ' if obj1 == obj2 else ' not '}equal {obj2}")
