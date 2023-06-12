numbers = ""
for i in range(100):
    numbers += "{:02d}".format(i)
    if i != 99:
        numbers += ", "
print(numbers)
