n, x = map(int, input().split())
a = map(int, input().split())
print(*filter(lambda e: e < x, a))
