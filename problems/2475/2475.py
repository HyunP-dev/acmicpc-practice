def square(n: int) -> int:
    return n * n


def validate(*num):
    return sum(list(map(square, num))) % 10


print(validate(*map(int, input().split())))
