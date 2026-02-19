n = int(input())
for _ in range(n):
    data, check_bit = map(int, input().split())
    print(bin(data)[2:].count("1") % 2 == check_bit and "Valid" or "Corrupt")
