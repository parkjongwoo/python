from bs4 import BeautifulSoup

html_doc ="""<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body></html>"""

bs = BeautifulSoup(html_doc, 'html.parser')
print(bs)#파싱된 데이터 전체 출력
print(bs.title)#tag 반환
print(bs.title.name)
print(bs.title.string)#tag내 문자열 반환
print(bs.p)#같은 tag중 첫번째만 반환
print(bs.p['class'])#attribute 반환
print(bs.a)# 첫 tag만 반환
print(bs.find_all('a')) #모든 tag list형으로 반환
print(bs.find(id='link3')) #id 기준으로 검색

for link in bs.find_all('a'):
    print(link['href'])
