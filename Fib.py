from time import time, sleep
from sys import stdout

def time_func(func):
    cumulative_time = {"total": 0}

    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        cumulative_time["total"] += end_time - start_time
        print(f"{result}: Cumulative execution time for {func.__name__}: {(cumulative_time['total'])*1000:.6f} milliseconds", end="\r")
        return result

    return inner

def cache(func):
    cache=dict()
    def inner(arg):
        if arg in cache.keys():
            return cache[arg]
        res=func(arg)
        cache.update({arg: res})
        return res
    return inner

#@cache
@time_func
def FIB1(num):
    'recursive backtracking (top down)'
    match num:
        case 0: return 0
        case 1: return 1
    return FIB1(num-1) + FIB1(num-2)


@time_func
def FIB2(num):
    'Tabulation (bottom up)'
    base=[0,1]
    for i in range(2,num+1):
        base.append(base[i-1]+base[i-2])
    return base[-1]

print(FIB1(32))
print(FIB2(32))
