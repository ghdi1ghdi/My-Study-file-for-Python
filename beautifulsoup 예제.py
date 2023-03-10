from bs4 import BeautifulSoup
with open("example.html")as fp:
    soup = BeautifulSoup(fp,'html.parser')
import urlib.request
import urlib.parse

with urlib.request.urlopen(dodam.sjeduhs.kr/cop/bbs/selectBoardList.do?bbsId=BBSMSTR_000000016362&menuId=MNU_0000000000016813&sso=ok)as response:
    html=response.read()
    soup=BeautifulSoup(html,'html.parser')
