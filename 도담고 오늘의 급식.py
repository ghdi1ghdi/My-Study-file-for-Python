import re
import getopt
import sys
import requests
from bs4 import BeautifulSoup

print ("오늘의 급식:\n")

url = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%8F%84%EB%8B%B4%EA%B3%A0")
soup = BeautifulSoup(url.text, "lxml")
food = soup.find("ul", { "valign" : "middle" })

pattern = '	'
text = food.text

match = re.search(pattern, text)
startIndex = match.start()
endIndex = match.end()

result = '{}'.format(
	text[startIndex:endIndex+40]
)

print(result.strip())


pattern = '열량:'
text = food.text

match = re.search(pattern, text)
startIndex = match.start()
endIndex = match.end()

result1 = '{}'.format(
	text[startIndex:endIndex+10]
)

print(result1)
