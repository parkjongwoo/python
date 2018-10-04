
#파일 생성 w 로 쓰기모드로 파일 생성(기존에 내용이 존재하는 파일은 내용이 삭제됨)
# f=open('d:/python/test.txt','w')
#
# f.write('오호호호\nㄴㅇㄹㄴㅇㄹ')
# f.close()


#파일 읽기 r 로 읽기모드로 파일 열기
f=open('d:/python/test.txt','r')

while(1):
    line = f.readline()
    if not line:
        break
    print(line)

f.close()

#파일에 추가 쓰기를 할 경우는 a로 읽은 후 쓰기모드? 로 열기
# f=open('d:/python/test.txt','a')
# f.write("다시 열었습니다.")
# while(1):
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f.close()


# with open('d:/python/test.txt','w') as f:
#     f.write("with로 열었습니다.")