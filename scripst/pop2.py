# List of squares

number = int(input())
nums = 1
while nums <= number:
    if nums ** 2 <= number:
        print(nums**2)
    nums += 1

# Least divisor

num = int(input())
num_list = []
div = 1
while div <= num:
    if (num % div == 0) and (div > 1):
        num_list.append(div)
    div += 1
print(min(num_list))

# The Power of Two

N = int(input())
num_list = []
div = 1
while div <= N:
    if 2**div <= N:
        num_list.append(div)
print(max(num_list), 2**max(num_list))

# Morning jog

X = int(input())
Y = int(input())
days = 1
while X < Y:
    X *= 1.1
    days += 1
print(days)

# The length of the sequence

N = None
lenght = 0
while N != 0:
    N = int(input())
    if N != 0:
        lenght += 1
print(lenght)

# The sum of the sequence

N = None
sum = 0
while N != 0:
    N = int(input())
    sum += N
print(sum)

# The average of the sequence

N = None
sum = 0
n_e = 0
while N != 0:
    N = int(input())
    if N == 0:
        break
    sum += N
    n_e += 1
print(sum / n_e)

# The maximum of the sequence

N = None
large = 0
while N != 0:
    N = int(input())
    if N > large:
        large = N
print(large)

# The index of the maximum of a sequence

N = None
index = 0
l_index = 0
large = 0
while N != 0:
    N = int(input())
    index += 1
    if N > large:
        large = N
        l_index = index
print(l_index)
