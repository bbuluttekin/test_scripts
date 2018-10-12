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
