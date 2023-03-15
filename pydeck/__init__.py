from colored import fg, attr
import time


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
                  f'{f.__qualname__}({kwargs}) {result} == {expected_result} {fg(160)}Failed{attr(0)} in {time.time() - s}s!')
        else:
            print(f'{fg(227)}{attr("bold")}Test{attr(0)} '
                  f'{f.__qualname__}({kwargs}) {result} == {expected_result} {fg(40)}Passed{attr(0)} in {time.time()- s}s!')
        return f
    return decorator


