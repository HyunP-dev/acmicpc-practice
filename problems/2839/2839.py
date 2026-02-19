from functools import cache


@cache
def f(n: int) -> int:
    if n in [4, 7]:
        return -1
    if n in [3, 5]:
        return 1
    if n in [6, 8, 10]:
        return 2
    if n in [9, 11, 13]:
        return 3
    if n in [12, 14]:
        return 4
    
    b3 = f(n - 3)
    b5 = f(n - 5)
    if b3 > 0 or b5 > 0:
        b3 = b3 if b3 > 0 else 0
        b5 = b5 if b5 > 0 else 0
        return min(b3 + 1, b5 + 1)
    else:
        return -1


def main():
    n = int(input())
    t = 0
    if n > 60:
        t = (n - 30) // 5
        n -= t * 5
    result = f(n)
    if result < 0:
        print(-1)
    else:
        print(t + f(n))

main()
