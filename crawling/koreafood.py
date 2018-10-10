#url 요청시 사용하는
import urllib.request
import datetime
import json

from crawling.config import  *

from bs4 import BeautifulSoup

from urllib import request
from urllib.request import urlopen

import pandas as pd

import folium
import webbrowser
import numpy as np

from PIL import Image


#### url 받아 요청 실행
#### Naver Map API 형식에 맞춰 요청 보냄
def get_request_url(url,client_id,client_secret):
    req = request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = request.urlopen(req)

        if response.getcode() == 200:
            print("{} Url Request Success".format(datetime.datetime.now()))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("%s Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def main():
    # 웹 페이지 크롤링 작업
    url = "http://korean.visitkorea.or.kr/kor/bz15/food/w_royal_list.jsp"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    # css selector 방식
    doc = soup.select('#content > .doc .restaurant a')

    list_restaurant = []
    
    # dictionary list 형식으로 데이터 생성 ex) [{},{},{}]
    # http://korean.visitkorea.or.kr 에서 레스토랑 url,이름 목록 가져오기
    for idx, atag in enumerate(doc):
        item = dict({})
        # item['idx'] = idx
        item['url'] = atag['href']
        item['title'] = atag.img['alt'].split(',')[0]
        list_restaurant.append(item)

    # 위 레스토랑 url을 다시 크롤링하여 각 레스토랑의 주소, 좋아요 값 가져와서 추가
    for restaurant in list_restaurant:
        bs = BeautifulSoup(urlopen(restaurant['url']), 'html.parser')
        restaurant['addr'] = bs.select('div.thumbWrap figure figcaption ul li')[0].span.string
        restaurant['like'] = bs.select('div.cnt_head ul li.likebutton button')[0].string

    # 각 레스토랑의 주소를 기준으로 Naver API에서 위,경도 값 가져와서 추가
    for restaurant in list_restaurant:
        encText = urllib.parse.quote(restaurant['addr'])
        url = "https://openapi.naver.com/v1/map/geocode?query=" + encText  # json 결과
        res = get_request_url(url, client_id, client_secret)
        json_result = json.loads(res)
        item_point = json_result['result']['items'][0]['point']
        restaurant['x'] = item_point['x']
        restaurant['y'] = item_point['y']
        # print(res)

    ## 생성한 데이터 기준으로 맵 마커 생성
    
    # 맵 중앙 좌표를 각 지점의 평균값으로, 배율을 7 기준으로 하여 맵 생성
    mapping = folium.Map(location=[np.mean([float(d['y']) for d in list_restaurant]), np.mean([float(d['x']) for d in list_restaurant])], zoom_start=7)
    
    # 생성한 맵에 각 데이터 기준으로 마커 생성
    for item in list_restaurant:
        folium.Marker([item['y'], item['x']], popup=item['title']+' <br/><b>추천</b> '+item['like']).add_to(mapping)
    
    # 생성한 맵을 html파일로 내보내기
    mapping.save('d:/python/crawling/bs4_korea_food_map.html')
    # 웹브라우저에서 열기
    webbrowser.open('d:/python/crawling/bs4_korea_food_map.html')
    # print(list_restaurant)
    # return list_restaurant
    
    # dictionary list를 DataFrome 으로 변환
    df = pd.DataFrame(data=list_restaurant)
    
    # DataFrame 으로 csv파일 생성
    # columns= 컬럼명 리스트, index_label= index로 사용할 컬럼의 컬럼명을 지정. sep=컬럼 구분자,csv이므로 ','로 지정
    # index 컬럼에 관하여: dictionary list를 데이터 형식으로 정했는데 DataFrame생성시 index 값이 자동으로 붙는다.
    # 그러나 index값만 있고 컬럼명이 없는 상태로 생성되어 버린다.
    # 이를 csv로 변환시 index컬럼명이 없으므로 컬럼명과 데이터의 갯수가 다르게 된다
    # 그러므로 csv 생성시 index=False 로 지정하여 index컬럼 없이 csv를 생성하던지, index_label을 지정하여 index컬럼에 명칭을 넣어주던지 처리가 필요하다
    df.to_csv('best_korea_food.csv', sep=',', encoding='utf-8', columns=list_restaurant[0].keys(), index_label='idx')


if __name__=='__main__':
    main()





