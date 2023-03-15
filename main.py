from pydeck import Test

class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age 
    def output(self) -> str:
        return f'{self.name}({self.age})'

@Test('Alex(18)', name='Alex', age=18)
def test_person(name: str, age: int) -> str:
    person = Person(name, age)
    return person.output()

def square(x: int) -> int:
    return x**2


@Test(3136, x=55)
@Test(4, x=2)
def test_sqaure(x):
    return square(x)


