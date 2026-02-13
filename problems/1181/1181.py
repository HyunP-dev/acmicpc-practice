from functools import cmp_to_key


def compare(str1, str2):
    if len(str1) > len(str2):
        return 1
    if len(str1) == len(str2):
        if str1 > str2:
            return 1
        if str1 == str2:
            return 0
        if str1 < str2:
            return -1
    if len(str1) < len(str2):
        return -1 
    
n = int(input())
words = set()
for _ in range(n):
    words.add(input())
for word in sorted(words, key=cmp_to_key(compare)):
    print(word)
