import re

expr = input()
expr = re.sub(r"\b0+(?=\d)", "", expr)

min_ = eval("-".join(map(str, [eval(subexpr) for subexpr in expr.split("-")])))
print(min_)
