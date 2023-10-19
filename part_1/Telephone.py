phone_number = str(input())
number_1 = str(input())
number_2 = str(input())
number_3 = str(input())

numbers = [phone_number, number_1, number_2, number_3]

for i in range(4):
    numbers[i] = numbers[i].replace("+7", '8')
    numbers[i] = numbers[i].replace("-", '')
    numbers[i] = numbers[i].replace("(", '')
    numbers[i] = numbers[i].replace(")", '')
    if len(numbers[i]) == 7:
        numbers[i] = "8495" + numbers[i]

phone_number = numbers[0]
for i in range(1, 4):
    if phone_number == numbers[i]:
        print("YES")
    else:
        print("NO")
