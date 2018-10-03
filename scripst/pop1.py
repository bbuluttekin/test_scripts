# Sum of three numbers
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# Area of right-angled triangle

b = int(input())
h = int(input())
print(b * h / 2)

# Apple sharing

n = int(input())
k = int(input())
print(k // n)
print(k % n)

# Hello, Harry!

name = input()
print('Hello, {}!'.format(name))

# Previous and next

num = int(input())
print('The next number for the number {} is {}'.format(num, num + 1))
print('The previous number for the number {} is {}'.format(num, num - 1))

# School desks

class_1 = int(input())
class_2 = int(input())
class_3 = int(input())
print((class_1 // 2) + (class_1 % 2) + (class_2 // 2) +
      (class_2 % 2) + (class_3 // 2) + (class_3 % 2))

# Last digit of integer

num = input()
print(num[-1])

# Tens digit

num = int(input())
print((num % 100) // 10)

# Sum of digits

num = input()
print(int(num[0]) + int(num[1]) + int(num[2]))
