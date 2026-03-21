n = int(input())
points = []
for _ in range(n):
    points.append(tuple(map(int, input().split())))
for point in sorted(points):
    print(*point)
