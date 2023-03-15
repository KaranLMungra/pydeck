from pydeck import Test, Tests

class Person:
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age 
    def output(self) -> str:
        return f'{self.name}({self.age})'

@Tests(['Alex(19)', 'Per(20)'], [{'name': 'Alex', 'age': 19}, {'name': 'Per', 'age': 20}])
@Test('Alex(18)', name='Alex', age=18)
def test_person(name: str, age: int) -> str:
    person = Person(name, age)
    return person.output()

def square(x: int) -> int:
    return x**2

@Tests([x**2 for x in range(1,20)], [{"x":x} for x in range(1, 20)])
@Test(3136, x=56)
@Test(4, x=2)
def test_sqaure(x):
    return square(x)


