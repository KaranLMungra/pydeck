from colored import fg, attr
import time
import tqdm

__COLOR_PASSED = fg(40)
__COLOR_TEXT = fg(227)
__COLOR_FAILED = fg(160)

COLOR_PASSED = fg(40)
COLOR_TEXT = fg(227)
COLOR_FAILED = fg(160)


def __check_arg_types(f, expected_result, kwargs: dict):
    for key in f.__annotations__.keys():
        if key == 'return':
            if not f.__annotations__[key] == type(expected_result):
                raise TypeError
            continue
        if not f.__annotations__[key] == type(kwargs[key]):
            raise TypeError


def Test(expected_results: list, args: list):
    assert len(expected_results) == len(args)
    assert len(expected_results) > 0

    def decorator(f):
        total = 0.0
        if len(expected_results) == 1:
            s = time.time()
            __check_arg_types(f, expected_results[0], args[0])
            result = f(**args[0])
            e = time.time()
            total += (e-s)
            if not result == expected_results[0]:
                print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                      f'{f.__qualname__}({args[0]}) {result} == {expected_results[0]} {COLOR_FAILED}Failed{attr(0)} in {time.time() - s}s!', end='\n\n')
                raise AssertionError
            else:
                print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                      f'{f.__qualname__}({args[0]}) {result} == {expected_results[0]} {COLOR_PASSED}Passed{attr(0)} in {time.time()- s}s!', end='\n\n')
            return f
        test_failed = -1
        for i in tqdm.trange(len(expected_results)):
            s = time.time()
            __check_arg_types(f, expected_results[i], args[i])
            result = f(**args[i])
            e = time.time()
            total += (e - s)
            if not result == expected_results[i]:
                test_failed = i
                break
        if test_failed != -1:
            result = f(**args[test_failed])
            print(f'{__COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                  f'{f.__qualname__}({args[test_failed]}) {result} =='
                  f'{expected_results[test_failed]} {__COLOR_FAILED}Failed{attr(0)}!', end='\n\n')
            raise AssertionError
        else:
            print(f'{__COLOR_TEXT}{attr("bold")}All Test of{attr(0)} '
                  f'{f.__qualname__}({args[0]}...) {__COLOR_PASSED}Passed{attr(0)} in {total}!', end='\n\n')
        return f
    return decorator


class PyDeck:
    def __init__(self) -> None:
        self.tests = {}

    def test(self):
        for func_name in self.tests.keys():
            f = self.tests[func_name]['fn']
            tests = self.tests[func_name]['tests']
            for expected_result, kwargs in tqdm.tqdm(tests):
                s = time.time()
                result = f(**kwargs)
                if not result == expected_result:
                    print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                          f'{func_name}({kwargs}) {result} == {expected_result} {COLOR_FAILED}Failed{attr(0)} in {time.time() - s}s!', end='\n\n')
                    raise AssertionError
                else:
                    print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                          f'{func_name}({kwargs}) {result} == {expected_result} {COLOR_PASSED}Passed{attr(0)} in {time.time()- s}s!', end='\n\n')

    def add(self, f, expected_result, kwargs):
        if f.__qualname__ not in self.tests:
            self.tests[f.__qualname__] = {
                'fn': f,
                'tests': []
            }

        self.tests[f.__qualname__]['tests'].append((expected_result, kwargs))


def PyDeckTest(deck: PyDeck, expected_result, **kwargs):
    def decorate(f):
        __check_arg_types(f, expected_result, kwargs)
        deck.add(f, expected_result, kwargs)
        return f
    return decorate
