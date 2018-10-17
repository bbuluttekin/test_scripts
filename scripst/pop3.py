# Even indices

my_list = input()
my_list = my_list.split(' ')
for item in range(len(my_list)):
    if item % 2 == 0:
        print(my_list[item])

# Even elements

my_list = input()
my_list = my_list.split(' ')
for item in my_list:
    if int(item) % 2 == 0:
        print(item)

# Greater than previous

my_list = input()
my_list = my_list.split(' ')
for item in range(len(my_list)):
    if item != 0:
        if int(my_list[item]) > int(my_list[(item - 1)]):
            print(my_list[item])

# Neighbors of the same sign

my_list = input()
my_list = my_list.split(' ')
for item in range(len(my_list) - 1):
    if (int(my_list[item]) > 0) and (int(my_list[item + 1]) > 0):
        print(my_list[item], my_list[item + 1])
        break
    elif (int(my_list[item]) < 0) and (int(my_list[item + 1]) < 0):
        print(my_list[item], my_list[item + 1])
        break
    else:
        print()

# Greater than neighbours

my_list = input()
my_list = my_list.split(' ')
i_list = 0
for i in range(len(my_list)):
    if i != 0 and i != (len(my_list) - 1):
        c_1 = int(my_list[i - 1]) < int(my_list[i])
        c_2 = int(my_list[i]) > int(my_list[i + 1])
        if c_1 and c_2:
            i_list += 1
print(i_list)

# The largest element

my_list = input()
my_list = my_list.split(' ')
i_list = []
for i in my_list:
    i_list.append(int(i))
print(max(i_list), i_list.index(max(i_list)))

# The number of distinct elements

my_list = input()
my_list = my_list.split(' ')
i_list = []
for item in my_list:
    i_list.append(int(item))
print(len(set(i_list)))

# Swap neighbours

my_list = input()
my_list = [int(i) for i in my_list.split(' ')]
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
for item in my_list:
    print(item)

# Swap min and max

my_list = input()
my_list = my_list.split(' ')
i_list = []
for item in my_list:
    i_list.append(int(item))
i_max = i_list.index(max(i_list))
i_min = i_list.index(min(i_list))
my_list[i_max] = str(min(i_list))
my_list[i_min] = str(max(i_list))
for item in my_list:
    print(item)

# The number of pairs of equal

L = [int(x) for x in input().split(' ')]
c = 0
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] == L[j]:
            c += 1
print(c)

# Unique elements

my_list = input()
my_list = my_list.split(' ')
for i in range(len(my_list)):
    if my_list[i] in my_list[i + 1:] or my_list[i] in my_list[:i]:
        continue
    else:
        print(my_list[i])

# Queens

A = 8
x = []
y = []
for item in range(A):
    x_l, y_l = [int(i) for i in input().split(' ')]
    x.append(x_l)
    y.append(y_l)
status = True
for i in range(A):
    for j in range(i + 1, A):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            status = False
if status:
    print('NO')
else:
    print('YES')

# The bowling alley

N, K = [int(x) for x in input().split()]
C = ["I"] * N
for item in range(K):
    l, r = [int(x) for x in input().split()]
    for i in range(l - 1, r):
        C[i] = '.'
print(''.join(C))

# Slices

c_str = input()
print(c_str[2])
print(c_str[-2])
print(c_str[:5])
print(c_str[:-2])
print(c_str[::2])
print(c_str[1::2])
print(c_str[::-1])
print(c_str[::-2])
print(len(c_str))

# The number of words

S = input()
print(S.count(" ") + 1)

# The first and last occurrence

S = input()
if S.count('f') == 1:
    print(S.find("f"))
elif S.count("f") >= 2:
    print(S.find("f"), S.rfind("f"))

# Reverse the fragment

S = input()
H = S[:S.find("h")]
H_i = S[S.find("h"):S.rfind("h") + 1]
H_ii = S[S.rfind("h") + 1:]
S = H + H_i[::-1] + H_ii
print(S)

# Replace within the fragment

S = input()
S_i = S[:S.find('h') + 1]
S_ii = S[S.find('h') + 1:S.rfind('h')]
S_iii = S[S.rfind('h'):]
S = S_i + S_ii.replace('h', 'H') + S_iii
print(S)

# Delete every third character

S = input()
x = ''
for item in range(len(S)):
    if item % 3 != 0:
        x = x + S[item]
print(x)
