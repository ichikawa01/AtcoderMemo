# メモ化再帰(@cache)
from functools import cache

cnt = 0
@cache
def f(n):
    global cnt
    cnt += 1
    if n<=1:
        return n
    return f(n-1) + f(n-2)
fib4=f(3)
print('fib4=',fib4)
print('fib4_cnt=',cnt)