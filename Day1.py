number1 = []
number2 = []
Total = 0
count = 0


with open("input.txt","r") as file:
        List = file.readlines()

for item in List:
        num1, num2 = item.split("  ")
        number1.append(num1)
        num2 = num2.rstrip("\n").lstrip(" ")
        number2.append(num2)



for number in number1:
        for numbers in number2:
                if number == numbers:
                        count += 1


        Total = Total + (int(number) * count)
        count = 0

print(Total)
