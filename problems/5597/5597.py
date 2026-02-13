students = {int(input()) for _ in range(28)}
print("\n".join(map(str, students ^ set(range(1, 31)))))