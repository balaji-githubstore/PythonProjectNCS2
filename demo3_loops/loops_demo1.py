# print number 1 to 10

# for i in range(1, 11):
#     print(i)

numbers = [78, 66, 88, 22, 32, 8, 77, 7, 99, 9, 11, 30]

size = len(numbers)

print(size)

for num in range(0, len(numbers)):
    print(numbers[num])

print("*" * 50)

# 1.	Print only numbers less than or equal to 50 from below list
# numbers = [78, 66, 88, 22, 32, 8, 77, 7, 99, 9,11,30]
for i in range(0, len(numbers)):
    if numbers[i] <= 50:
        print("the value is ")
        print(numbers[i])
