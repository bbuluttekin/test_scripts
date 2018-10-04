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

# Fractional part

num = float(input())
print(num - int(num))

# First digit after decimal point

num = float(input())
print(int((((num - int(num)) * 100) - (((num - int(num)) * 100) % 10)) // 10))

# Car route

n = int(input())
m = int(input())
print((m // n) + (m % n != 0))

# Digital Clock

n = int(input())
print(n // 60, n % 60)

# Total Cost

A = int(input())
B = int(input())
N = int(input())
print((A * N + (B * N) // 100), (B * N) % 100)

# Clock Face-1

h = int(input())
m = int(input())
s = int(input())
print(30 * h + 30 / 60 * m + 30 / 3600 * s)

# Clock Face-2

A = float(input())
print(A % 30 * 12)

# Minimum of two numbers

num_1 = int(input())
num_2 = int(input())
print(min(num_1, num_2))

# Sign function

int_x = int(input())
if int_x > 0:
    print(1)
elif int_x < 0:
    print(-1)
else:
    print(0)
