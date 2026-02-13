n, m = map(int, input().split())


A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

C = [[None for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]

for i in range(n):
    for j in range(m):
        print(C[i][j], end=" ")
    print()