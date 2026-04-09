import json
from collections import deque

t = int(input())
for _ in range(t):
    p = input()
    p = p.replace("RR", "")
    n = int(input())
    arr = deque(json.loads(input()))

    is_rev = False
    for f in p:
        if f == "R":
            is_rev = not is_rev
        else:
            if arr:
                if not is_rev:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                arr = None
                break
    if arr is None:
        print("error")
    else:
        if is_rev:
            arr.reverse()
        print(str(arr).replace(" ", "")[6:-1])
