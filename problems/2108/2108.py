import statistics
from collections import Counter

def init():
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    return arr


def mode(arr):
    most_common = Counter(arr).most_common()
    _, mc = most_common[0]
    m = sorted([(v, c) for (v, c) in most_common if c == mc], key=lambda p: p[0]) 
    if len(m) == 1:
        return m[0][0]
    else:
        return m[1][0]

def display(arr):
    print(round(statistics.mean(arr)))
    print(statistics.median(arr))
    print(mode(arr))
    print(max(arr) - min(arr))


def main():
    arr = init()
    display(arr)


if __name__ == "__main__":
    main()
