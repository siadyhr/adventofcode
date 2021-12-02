with open("in") as f:
    numbers = f.readlines()
numbers = [int(number) for number in numbers]
for i, number1 in enumerate(numbers):
    for number2 in numbers[:i] + numbers[i:]:
        if number1 + number2 == 2020:
            print(number1*number2)
