# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("input.txt", "r")

T = int(input())
#좌표정보
datas = []
#웜홀정보
wormhole = {}
# 계산중인 현재위치 정보 : p-좌표,d-방향(udlr),l:같은점수목록,n-다음좌표
currentPoint = {'p': None, 'd': None, 'l': None, 'n': None}
# 이동중인 커서 정보 : p-좌표,d-방향(udlr),s-획득된 점수
cursorPoint = {'p': None, 'd': None, 's': 0}
# 점수 목록 : 상하좌우 = key:(x,y), value: score
score_dic = {'u': {}, 'd': {}, 'l': {}, 'r': {}}
#최고 점수
score_best = 0

# 방향+블록에 따른 이동 값
nextp_90 = None
nextp_180 = None

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


# def str_to_int(str_list):
#     int_list = []
#     for item in str_list:
#         if item is '':
#             break
#         int_list.append(int(item))
#
#     return int_list
def str_to_int(str_list):
    int_list = []
    for item in str_list:
        if item is '':
            break
        int_list.append(int(item))

    return int_list

def getWormholeDic(data):
    result = None
    cnt = len(data)
    for r in range(cnt):
        if data[r] >= 6:
            if result is None:
                result = {}
            if data[r] not in result:
                result[data[r]] = []
            result[data[r]].append(r)
    return result


def getwormholeexit(holelist,inpoint):
    if holelist.index(inpoint) == 0:
        return holelist[1]
    else:
        return holelist[0]

# def procScore():


for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    # 탐색시 방향 정보
    dir_info = {'r':{'s': 0, 'e': N*N-1},'ㅣ':{'s': N*N-1, 'e': 0},'u':{ 's': N*N-1, 'e': (0, 0)},'d':{ 's': 0, 'e': N*N-1}}

    # 점수 산정시 방향+블록에 따른 이동 값
    nextp_90 = {('r', 3): (N, 'd'), ('r', 4): (-N, 'u'),
                ('l', 1): (-N, 'u'), ('l', 2): (N, 'd'),
                ('u', 2): (1, 'r'), ('u', 3): (-1, 'l'),
                ('d', 1): (1, 'r'), ('d', 4): (-1, 'l')}
    nextp_180 = {'r': (-1, 'l'), 'l': (1, 'r'), 'u': (N, 'd'), 'd': (-N, 'u')}

    for row_idx in range(N):
        row = input()
        datas.extend(str_to_int(row.split(' ')))

    wormhole = getWormholeDic(datas)
    print(wormhole)
    #print(getwormholeexit(wormhole[7],wormhole[7][1]))

    for idx in range(N*N-1):
        if datas[idx] != 0:
            continue

        score_best = max(procScore(datas, idx, 'r', 0),score_best)


    currentPoint.clear()
    currentPoint.clear()
    cursorPoint.clear()
    score_dic.clear()
    datas.clear()
    del wormhole

    print('# {} {}'.format(test_case,score_best))
    score_best = 0

    # ///////////////////////////////////////////////////////////////////////////////////
