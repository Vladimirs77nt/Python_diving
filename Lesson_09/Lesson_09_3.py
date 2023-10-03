import random
from typing import Callable

def cache(func: Callable):
    # _cache_dict = {}
    _cache_dict = []
    def wrapper(*args):
        if args not in _cache_dict:
            # _cache_dict[args] = func(*args)
            _cache_dict.append (func(*args))
        # return _cache_dict[args]
        return _cache_dict
    return wrapper

@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 10) = }')