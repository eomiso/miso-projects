# sums.py
# add the numbers in `data.txt`

sum = 0.0

with open("data.txt") as file:
    for line in file:
        number = float(line)
        sum += number

print(f"{sum:.2f}")
