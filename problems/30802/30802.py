from math import ceil

n = int(input())
ts = list(map(int, input().split()))
t, p = map(int, input().split())

ts = map(lambda subt: ceil(subt / t), ts)
print(sum(ts))
print(*divmod(n, p))
