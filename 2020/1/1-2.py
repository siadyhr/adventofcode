with open("in") as f:
    numbers = f.readlines()
numbers = [int(number) for number in numbers]
for i, number1 in enumerate(numbers):
    subnumbers = numbers[:i] + numbers[i:]
    for j, number2 in enumerate(subnumbers):
        for number3 in subnumbers[:j] + subnumbers[j:]:
            if number1 + number2 + number3 == 2020:
                print(number1*number2*number3)
