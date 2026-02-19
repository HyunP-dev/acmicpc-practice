def f(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return f(n - 1) + f(n - 2) + f(n - 3)


t = int(input())
for _ in range(t):
    n = int(input())
    print(f(n))
