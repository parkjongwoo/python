def sum(a,b):
    return a+b

def suml(a,b):
    return a+b,a*b#### tuple 데이터형 반환 :: 오해 금지

## 인수를 여러개 튜플로 받는 경우
def sum(*args):
    tot = 0
    for i in args:
        tot += i

    return tot

print(sum(1,2))
print(suml(1,2))

print(sum(1,2,3,4,5,6,7,8,9,10))

##  key,value 쌍으로 이루어진 인수를 튜플로 받는 경우는 ** 사용
## 아래와 같이 동시에 여러개의 여러 인수를 받는 경우는 호출시 순서가 섞이면 안됨
## *,** 인수는 같은 것을 중복 사용 불가
def func(*args, **kvargs):
    print(args)
    print(kvargs)


def default(man=True):
    print(man)

def default2(name, age, man=True):#초기값 있는 함수는 끝에 사용
    print(name + str(man) + str(age))
    
func(1,2,3,4,5,name='samyong',age=17,score=11,zender='male')
default()
default(False)

default2('홍', False, 18)