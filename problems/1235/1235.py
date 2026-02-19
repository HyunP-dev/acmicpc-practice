n = int(input())
ids = [input() for _ in range(n)]
for i in range(1, len(ids[0]) + 1):
    if len({id[-i:] for id in ids}) == n:
        print(i)
        break
