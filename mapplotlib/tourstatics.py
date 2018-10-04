import urllib
from urllib import request, parse
import datetime
import json

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

from mapplotlib.config import *

import matplotlib.font_manager as fm

#### url 받아 요청 실행
def get_request_url(url):
    req = request.Request(url)

    try:
        response = request.urlopen(req)

        if response.getcode() == 200:
            print("{} Url Request Success".format(datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("%s Error for URL : %s" % (datetime.datetime.now(), url))
        return None

##### 연도,국가,외국인/내국인 인수를 받아 요청 처리
def getNatVisitor(ym,nat_cd,ed_cd):

    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM="+ym+"&NAT_CD="+nat_cd+"&ED_CD="+ed_cd

    url = end_point + parameters
    #print(url)
    reData = get_request_url(url)
    if(reData is None):
        return None
    else:
        return json.loads(reData)

######### 시작, 끝 연도에 맞춰 '275', 'E' 데이터 요청하고 변수에 저장( 미국, 외국인국내 유입 인원)
datas = {}
start_y = 2015
end_y = 2016
for yyyy in range(start_y,end_y+1):
    y_str = str(yyyy)
    datas[y_str] = {}
    datas[y_str]["data"] = []
    datas[y_str]["month"] = []
    for mm in range(1,13):
        m_str = "{:02d}".format(mm)
        # axis_mm.add(m_str)
        json_result = getNatVisitor(y_str+m_str, '275', 'E')
        # print(json.dumps(json_result,indent=4,sort_keys=True,ensure_ascii=False))#json >string 변환시

        datas[y_str]["data"].append(json_result["response"]["body"]["items"]["item"]["num"])
        datas[y_str]["month"].append(mm)
        datas[y_str]["national"] = json_result["response"]["body"]["items"]["item"]["natKorNm"].replace(' ','')
        datas[y_str]["natCd"] = json_result["response"]["body"]["items"]["item"]["natCd"]
        datas[y_str]["edCd"] = json_result["response"]["body"]["items"]["item"]["edCd"]


# print(usa_visitors)
# print(axis_mm)
# print(datas)


# matplotlib.rc('font', family='malgunbd.ttf')

####### 설치된 폰트 전체 가져오기
# ttf 폰트 전체 가져오기
print([(f.name, f.fname) for f in fm.fontManager.ttflist ])
#### 전역 폰트 설정 : font.family 에는 폰트명을 지정
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 14
plt.rcParams["figure.figsize"] = (14,4)

fig, ax = plt.subplots()
ax.set_xticks(datas[str(start_y)]["month"])

for k, v in datas.items():
    # print(dic)
    plt.plot(v["month"], v["data"], 'r-')
    #plt.plot(datas["2015"]["month"], datas["2015"]["data"], 'r-', datas["2016"]["month"], datas["2016"]["data"], 'b-')


# plt.axis([],list[axis_mm])

plt.ylabel('방문수')
plt.xlabel('월')


plt.show()

# print(datas)

###### 파일로 json 형태 정보 저장
with open("{}에서 유입된 방문객 정보_{}_{}.json".format(datas[str(start_y)]["national"], start_y, end_y),'w',encoding='utf-8') as f:
    rejson = json.dumps(datas,indent=4,sort_keys=True,ensure_ascii=False)
    f.write(rejson)




# api_key = 'ndIfhEWF0WUvaDbFTRQ22d4v3dSlyEjp79gILqxlFopycWxNaamQddeFADBHEFUrhBuymXNjS4vdK9MAQz3GxA%3D%3D'
# url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
# queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : api_key, parse.quote_plus('YM') : '201201', parse.quote_plus('NAT_CD') : '112', parse.quote_plus('ED_CD') : 'D' })
#
# req = request.Request(url + queryParams)
# print(req.get_full_url())
# req.get_method = lambda: 'GET'
# response_body = request.urlopen(req).read()
# print(response_body)