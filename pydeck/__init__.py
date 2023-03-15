from colored import fg, attr
import time
import tqdm

def Test(expected_result, **kwargs):
    def decorator(f):
        s = time.time()
        for key in f.__annotations__.keys():
            if key == 'return':
                if not f.__annotations__[key] == type(expected_result):
                    raise TypeError
                continue
            if not f.__annotations__[key] == type(kwargs[key]):
                raise TypeError
        result = f(**kwargs)
        if not result == expected_result:
            print(f'{fg(227)}{attr("bold")}Test{attr(0)} '
                  f'{f.__qualname__}({kwargs}) {result} == {expected_result} {fg(160)}Failed{attr(0)} in {time.time() - s}s!', end='\n\n')
            raise AssertionError
        else:
            print(f'{fg(227)}{attr("bold")}Test{attr(0)} '
                  f'{f.__qualname__}({kwargs}) {result} == {expected_result} {fg(40)}Passed{attr(0)} in {time.time()- s}s!', end='\n\n')
        return f
    return decorator

def Tests(expected_results: list, args: list):
    assert len(expected_results) == len(args)
    def decorator(f):
        total = 0.0
        test_failed = -1
        for i in tqdm.tqdm(range(len(expected_results))):
            expected_result = expected_results[i]
            kwargs = args[i]
            s = time.time()
            for key in f.__annotations__.keys():
                if key == 'return':
                    if not f.__annotations__[key] == type(expected_result):
                        raise TypeError
                    continue
                if not f.__annotations__[key] == type(kwargs[key]):
                    raise TypeError
            result = f(**kwargs)
            e = time.time()
            total += (e - s)
            if not result == expected_result:
                test_failed = i
                break
                
        expected_result = expected_results[i]
        kwargs = args[i]
        result = f(**kwargs)
        if test_failed != -1:
            print(f'{fg(227)}{attr("bold")}Test{attr(0)} '
                    f'{f.__qualname__}({kwargs}) {result} == {expected_result} {fg(160)}Failed{attr(0)}!', end='\n\n')
            raise AssertionError
        else:
            print(f'{fg(227)}{attr("bold")}All Test of{attr(0)} '
                    f'{f.__qualname__} {fg(160)}Passed{attr(0)} in {total}!', end='\n\n')
        return f
    return decorator

