plates = input()
before = ""
sum_ = 0
for plate in plates:
    if plate != before:
        before = plate
        sum_ += 10
    else:
        sum_ += 5
print(sum_)
