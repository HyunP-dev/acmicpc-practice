def replacer(ch: str) -> str:
    if "a" <= ch <= "z":
        return ch.upper()
    else:
        return ch.lower()


s = input()
print("".join(map(replacer, s)))
