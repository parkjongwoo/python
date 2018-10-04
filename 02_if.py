money=input()
card = 1
try:
    money = int(money)
except:
    print("int 변경불가")

if money:
    print(str(money)+"는 참")
else:
    print(str(money)+"는 거짓")

if money> 1000 and money<3000: #and 연산
    print("점심값 수준")
else:
    print("많거나 적음")

if money<= 1000 or money>=3000:# or 연산
    print("많거나 적음")
else:
    print("점심값 수준")

if not card:#not 연산
    print("dd")
else:
    print("not 연산자는 java의 !연산과 동일")

list_pocket = ['cash','check','card']

if 'cash' in list_pocket:#pass는 아무런 동작이 없는 경우 사용
    pass
else:
    print("걸어가기")

if 'cash' in list_pocket:#pass는 아무런 동작이 없는 경우 사용
    print('택시')
elif 'check' in list_pocket:
    print('리무진')
else:
    print("걸어가기")


score = input()
try:
    score = int(score)
except:
    print("int 변경불가")

if score > 90:
    print("A학점")
elif score > 80:
    print("B학점")
elif score> 70:
    print("C학점")
elif score>60:
    print("D학점")
else:
    print("F학점")
