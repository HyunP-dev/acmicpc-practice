def dsum(n: int) -> int:
    return n + sum(map(int, str(n)))


def dsumof(n: int):
    for i in range(1, n + 1):
        if dsum(i) == n:
            return i
    return 0


n = int(input())
print(dsumof(n))
