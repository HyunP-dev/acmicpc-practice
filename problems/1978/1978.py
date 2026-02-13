from math import sqrt


def isprime(p: int) -> bool:
    if p <= 1:
        return False
    if p == 2 or p == 3 or p == 5:
        return True
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


input()
ps = map(int, input().split())
print(sum(list(map(isprime, ps))))
