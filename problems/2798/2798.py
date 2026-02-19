from itertools import combinations


n, m = map(int, input().split())
cards = map(int, input().split())
print(max(filter(lambda s: s <= m, map(sum, combinations(cards, 3)))))
