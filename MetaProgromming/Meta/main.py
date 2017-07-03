import time
from functools import  wraps

def timethis(func):
    '''
    decorator .
    '''
    @wraps(func)
    def wapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wapper

@timethis
def countdown(n : int):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1


countdown(100000)