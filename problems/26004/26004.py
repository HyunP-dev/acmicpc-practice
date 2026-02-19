from collections import Counter

n = int(input())
s = input()

print(min(Counter(s).get(ch, 0) for ch in "HIARC"))
