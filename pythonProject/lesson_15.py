#



# def sum_x2(num1, num2):
#     return (num1 + num2) * 2
#
#
# sum_x2_lambda = lambda num1, num2: (num1 +num2) * 2
#
# print(sum_x2(3, 3))
# print(sum_x2_lambda(3, 3))
#
# numbers = list(range(1, 100))
# print(numbers)
# #classic
# numbers2 = []
# for number in numbers:
#     if number % 2 == 0:
#         numbers2.append(number)
# print(numbers2)
# #lambda
# numbers3 = list(filter(lambda el: el % 2 == 0, numbers))
# print(numbers3)

# numbers = list(range(1, 100))
# print(numbers)
# print(sorted(numbers, reverse=True))

# numbers = list(range(1, 10))
# print(numbers)
# numbers2 = list(map(lambda number: number+10, numbers))
# print(numbers2)
# print(list(map(lambda number: number*number, numbers)))
# numbers3 = []
# for number in numbers:
#     numbers3.append(number * number)
# print(numbers3)


numbers = list(range(1, 1000))
print(numbers)
numbers2 = list(filter(lambda number: number % 2 == 0, numbers))
numbers3 = list(filter(lambda number: number % 10 == 0, numbers2))
numbers4 = list(filter(lambda number: number % 5 == 0, numbers3))
numbers5 = list(filter(lambda number: number % 100 == 0, numbers4))
print(numbers5)