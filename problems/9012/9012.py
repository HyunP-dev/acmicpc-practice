def is_vps(vps: str) -> bool:
    stack = list[str]()
    for bracket in vps:
        if bracket == "(":
            stack.append(bracket)
        else:
            try:
                if stack.pop() != "(":
                    return False
            except IndexError:
                return False
    return not stack


n = int(input())
for _ in range(n):
    print("YES" if is_vps(input()) else "NO")
