
def docstringtest(a,b):
    """
    doc string 연습을 위한 예제 입니다
    """
    print('doc string 연습입니다.')
    return a+b


print(1+1)

# dic test
dictest = []
if dictest.get(1):
    print(dictest[1])
#list형: 순서있음(index값에 의한 참조가능). 변경 가능.
list_a = [1,2,3,4,5]
list_b = [3,4,5,6,7]
list_c = [i for i in list_b if i in list_a]#교집합. set은 & 연산으로 교집합 지원하지만 list는 불가능.set으로 형변환후 &처리도 가능

print(list_a)
print(list_b)
print(list_c)

#tuple형: 순서있음(index값에 의한 참조가능). 변경 불가능.
tuple_a = (1,2,3,4,5)
tuple_b = (3,4,5,6,7)
tuple_c = (i for i in tuple_a if i in tuple_b)#교집합. set은 & 연산으로 교집합 지원하지만 list는 불가능.set으로 형변환후 &처리도 가능

print(tuple_a)
print(tuple_b)
print(tuple_c)


int_a = int(3)
int_b = int("3")
# int_c = int("3.5") # error 3.5 형변환 불가

print(int_a)
print(int_b)
# print(int_c)

str_a = str(1)
str_b = '1'
str_c = "1"
str_d = """ dfjslkdfj doc string 입니다. """

print(str_a)
print(str_b)
print(str_c)
print(str_d)
print(len(str_d))
print(docstringtest(5,6))


set_str = set("hello")
print(set_str)


