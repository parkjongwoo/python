#############################
#별그리기
print('가로 표시 갯수를 입력하세요')
col = int(input())

left_blank = int(col/2)
max_left_blank = left_blank
star_cnt = 1
star_dir = 1
star_max = col
star_str = ''


for i in range(col):
    for k in range(left_blank):
        star_str += ' '
    for j in range(star_cnt):
        star_str += '*'
    print(star_str)
    if star_cnt == col:
        star_dir *= -1

    star_cnt += (star_dir*2)
    left_blank -= star_dir
    star_str = ''