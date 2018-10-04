a=0
while a<3:
    print(a)
    a += 1

hit=0
while hit<11:
    print("나무를 {}번 찍었습니다.".format(hit))
    print("나무를 %d번 찍었습니다." % hit)
    if hit==10:
        print("나무가 쓰러졌다")
    hit += 1
