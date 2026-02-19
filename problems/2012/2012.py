n = int(input())
scores = list[int]()
for _ in range(n):
    scores.append(int(input()))
scores.sort()
rate = 0
for i, score in enumerate(scores):
    rate += abs(score - (i + 1))
print(rate)
