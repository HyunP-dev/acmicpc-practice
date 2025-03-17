n, m = map(int, input().split())
A = list(sorted(map(lambda e: int(e) - 1, input().split())))
is_safe = False
for t in A:
    m -= t
    if m <= 0:
        is_safe = True
        break
if is_safe:
    print("DIMI")
else:
    print("OUT")
