my_list = \
    [[1, 2, 3,4],
     [5, 6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

rotated = list(zip(*my_list[::-1]))

print(my_list)
print(rotated)

a = (1,2)
a[0] = 3