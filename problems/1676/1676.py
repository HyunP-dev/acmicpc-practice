def factorize(n: int) -> list[int]:
    factors = []
    if n == 1:
        return factors
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                factors.append(i)
                break
    return factors


def count(n: int):
    if n < 5:
        return 0
    if n == 5:
        return 1
    return count(n - 1) + factorize(n).count(5)


n = int(input())
print(count(n))
