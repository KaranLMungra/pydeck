from colored import fg, attr
import time
import tqdm

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

def Test(expected_result, **kwargs):
    def decorator(f):
        s = time.time()
        __check_arg_types(f, expected_result, kwargs) 
        result = f(**kwargs)
        if not result == expected_result:
            print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                  f'{f.__qualname__}({kwargs}) {result} == {expected_result} {COLOR_FAILED}Failed{attr(0)} in {time.time() - s}s!', end='\n\n')
            raise AssertionError
        else:
            print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                  f'{f.__qualname__}({kwargs}) {result} == {expected_result} {COLOR_PASSED}Passed{attr(0)} in {time.time()- s}s!', end='\n\n')
        return f
    return decorator

def Tests(expected_results: list, args: list):
    assert len(expected_results) == len(args)
    def decorator(f):
        total = 0.0
        test_failed = -1
        for i in tqdm.tqdm(range(len(expected_results))):
            s = time.time()
            __check_arg_types(f, expected_results[i], args[i]) 
            result = f(**args[i])
            e = time.time()
            total += (e - s)
            if not result == expected_results[i]:
                test_failed = i
                break
                
        expected_result = expected_results[i]
        kwargs = args[i]
        result = f(**args[i])
        if test_failed != -1:
            print(f'{COLOR_TEXT}{attr("bold")}Test{attr(0)} '
                    f'{f.__qualname__}({args[i]}) {result} == {expected_result} {COLOR_FAILED}Failed{attr(0)}!', end='\n\n')
            raise AssertionError
        else:
            print(f'{COLOR_TEXT}{attr("bold")}All Test of{attr(0)} '
                    f'{f.__qualname__} {COLOR_PASSED}Passed{attr(0)} in {total}!', end='\n\n')
        return f
    return decorator

