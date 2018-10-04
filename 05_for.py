list_=['one','two','three']

for i in "list":
    print(i)

for i in ("list",):
    print(i)


for i in list_:
    print(i)

list_list = [[1,2],[3,4],[5,6]]


for (i, j) in list_list:
    print(i+j)


l_score = [50,70,80,52,100]
i_tot = 0;

for i in l_score:
    if i>60:
        print('{}점 합격입니다.'.format(i))
        i_tot += 1
    else:
        print('{}점 불합격입니다.'.format(i))

print("총 합격생은 {}명 입니다".format(i_tot))