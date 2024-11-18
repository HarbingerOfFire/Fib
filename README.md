# Fib
With Fibonacci Day (11/23) coming up, I thought I would make a post on Fibonacci Numbers. If you don't know about the Fibonacci sequence it's very simple. It's a sequence of numbers where the next number in line is equal to the sum of the 2 previous numbers. So if we start with 0 and 1, the next number is 1, then 2, then 3, then 5 and so on. The sequence appears in nature, but I won't need to get into that.

Python teachers often use this as a beginner lesson. Most schools and resources teach a way that follow the definition exactly. This means you give a function the index of the sequence and in takes that index and figures out the number by adding the sums of the two previous numbers, which it must also calculuate, all the way down until it reaches 1 and 0. In python, this looks something like this:
```python3
def FIB1(num):
    'recursive backtracking (top down)'
    match num:
        case 0: return 0 #if index=0, return 0
        case 1: return 1 #if index=1, return 1
    return FIB1(num-1) + FIB1(num-2)
```
However, this can cause problems because it has to calculate the same number numerous times. This can lead to exponential (the Big-O complexity of O(2^n)). To fix this, we add a cache, or a memory, to the function. This cache stores values at different indexes that are already known. This way, we no longer have to recalculuate the values at those indexes because we have them stored and can pull from them. 
In python, we can use a decorator to cache and check the cache for us like this:
```python3
def cache(func):
    cache=dict()
    def inner(arg):
        if arg in cache.keys(): #check if the number is in the cache
            return cache[arg] #return the cached value if it is
        res=func(arg)
        cache.update({arg: res}) #cache the value if not already
        return res
    return inner

@cache
def FIB1(num):
    'recursive backtracking (top down)'
    match num:
        case 0: return 0
        case 1: return 1
    return FIB1(num-1) + FIB1(num-2)
```
This works in O(n) time, because it calculates up to the index. However, it still has to check the cache each time, which is it's own O(N) operation, adding more time. 
To fix this, we can implement the memory into the function itself by working from the other direction. Since we know the base case, we can work from those up to our index. This is not exactly how the sequence is defined, but still gives the same result. This method is called tabulation, or the bottom up method, and works in a true O(n) time. It can be seen like this:
```python3
def FIB2(num):
    'Tabulation (bottom up)'
    base=[0,1]
    for i in range(2,num+1):
        base.append(base[i-1]+base[i-2])
    return base[-1]
```
To really see the difference you can use a decorator like seen in [Fib.py](https://github.com/HarbingerOfFire/Fib/blob/main/Fib.py)

## Extra: Fib-Cipher
One of my favorite things to do with a fibonacci sequence is to change the base case numbers from 0, 1. This creates different results. if the two numbers are in the fibonacci sequence already, then it just shifts the sequence over, but in cases where you use two random numbers, it can give wildly different numbers. So, you can initialize the sequence with a different set of base case values that act as a key, and then apply some sort of transformation based on the numbers. A simple example is shown in [Fib_cipher.py](https://github.com/HarbingerOfFire/Fib/blob/main/Fib_cipher.py)
