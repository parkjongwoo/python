print('가로 표시 갯수를 입력하세요')
col = int(input())

#################################33
#반복문 3개 중첩

max_row = int(9 / col) if 9%col == 0 else int(9 / col) + 1
f_col = 1
l_col = f_col + col
for k in range(max_row):
    for i in range(1,10):
        for j in range(f_col,l_col):
            print(str(j)+"*"+str(i)+"="+str(i*j), end='\t')


        print()

    f_col = l_col
    l_col = min(l_col + col,10)

print()

################################
# 반복문 1개 사용

p_n = 1
col_min = 1 + (p_n-1) * col
col_max = col_min + col
col_n = col_min
row_n = 1
row_max = 9

while(col_n<10):
    print(str(col_n) + "*" + str(row_n) + "=" + str(col_n * row_n), end='\t')
    col_n += 1
    if col_n == col_max:
        if row_n == row_max:
            print()
            p_n += 1
            col_min = 1 + (p_n - 1) * col
            col_max = min(col_min + col,10)
            col_n = col_min
            row_n = 1
        else:
            print()
            col_n = col_min
            row_n += 1



