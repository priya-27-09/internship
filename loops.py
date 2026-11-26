for number in range(1, 6):
    print(number)
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
for number in range(1, 10):
    if number == 5:
        break
    print(number)
for number in range(1, 6):
    if number == 3:
        continue
    print(number)