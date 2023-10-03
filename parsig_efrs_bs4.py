from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from selenium import webdriver



url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=3BB911C104594D19AAF29E5D9E1065A7"

driver = webdriver.Chrome("")
driver.get(url)
html_code = driver.page_source # содержимое страницы
soup = bs(html_code,"html.parser")



oll_info = soup.find_all(class_="even")
oll_info1 = soup.find_all(class_="odd")
oll_info2 = soup.find_all(class_="primary")
oll_info3 = soup.find_all(class_="lotInfo")
find_all_td_align = soup.find_all('td', align="right")
# print()
print(*oll_info[1].text.split()[-3:]) # ФИО должника
print(*oll_info1[3].text.split()[1:]) # снилс Должника
print(oll_info[3].text.split()[-1]) # ИНН Должника
print(*oll_info1[2].text.split()[2:]) # место жительства
print(*oll_info[5].text.split()[2::]) # ФИО ИНН арбитражного упр
print(*oll_info[6].text.split()) # @mail орбитражного
print(oll_info1[-2].text.split()[-1]) # форма подачи пердложений о цене
print(oll_info[-1].text[16:]) # место проведения
print(oll_info[-4].text[10:]) # тип торгов
print(oll_info1[-1].text[0]) # номер лота
print(str(oll_info1[-1].text[1:]).title()) #наименование лота   
print(int(find_all_td_align[-1].text.split(",")[0])) # проценты от цены лота
print(str(find_all_td_align[-3].text.split(",")[0]).replace(" ","")) # начальная цена лота

# # for i in find_all_td_align:
# #     print(i.text)

# 