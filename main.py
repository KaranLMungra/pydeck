from pydeck import PyDeck, PyDeckTest, Test
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    def output(self) -> str:
        return f'{self.name}({self.age})'
class Hello:
    @staticmethod
    def printf(s):
        print(s)

@Test(['Alex(19)', 'Per(20)'], [{'name': 'Alex', 'age': 19}, {'name': 'Per', 'age': 20}])
def test_person(name: str, age: int) -> str:
    person = Person(name, age)
    return person.output()

def square(x: int) -> int:
    return x**2

@Test([x**2 for x in range(1,20)] + [3136, 4], [{"x":x} for x in range(1,
                                                                          20)] +
      [{"x": 56}, {"x": 2}])
def test_sqaure(x):
    return square(x)

deck = PyDeck()

@PyDeckTest(deck, 'World', msg='World')
@PyDeckTest(deck, 'Hello', msg='Hello')
def hello(msg: str) -> str:
    return msg

deck.test()


