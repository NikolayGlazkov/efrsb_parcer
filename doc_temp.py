import os
import datetime
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=3BB911C104594D19AAF29E5D9E1065A7"

driver = webdriver.Chrome("")
driver.get(url)
html_code = driver.page_source  # содержимое страницы
soup = bs(html_code, "html.parser")

oll_info = soup.find_all(class_="even")
oll_info1 = soup.find_all(class_="odd")
oll_info2 = soup.find_all(class_="primary")
oll_info3 = soup.find_all(class_="lotInfo")
find_all_td_align = soup.find_all("td", align="right")


# print(*oll_info[6].text.split()) # @mail орбитражного
efrsb_num = oll_info[0].text.split()[-1]  # номер публикации в ефрсб
efrsb_publice = oll_info1[0].text.split()[-1]  # дата публикации в ефрсб
todayis = datetime.date.today().strftime("%d.%m.%Y")  # дата сегодня
obligator = " ".join(oll_info[1].text.split()[-3:])  # ФИО должника
adres_of_oblig = " ".join(oll_info1[2].text.split()[2:])  # место жительства
arbitor_man = " ".join(oll_info[5].text.split()[2:-5])  # Фио Арбитражного упр.
obligator_snils = " ".join(oll_info1[3].text.split()[1:])  # снилс Должника
inn_arbit_man = " ".join(oll_info[5].text.split()[-4:-3])  # ИНН арбитражного упровляющего
snils_arbit_man = " ".join(oll_info[5].text.split()[-2::])
obligator_inn = " ".join(oll_info[3].text.split()[-1]).replace(" ", "")  # инн должника
elect_plase = oll_info[-1].text[16:]  # площадка проведения
proces = oll_info[-4].text[10:]  # тип процедуры
opn_clos = oll_info1[-2].text.split()[-1]  # метод проведения торгов откр. закр.
lot_namber = oll_info1[-1].text[0]  # номер лота
lot_name = str(oll_info1[-1].text[1:]).title()  #  имя лота
lot_price = str(find_all_td_align[-3].text.split(",")[0]).replace(" ", "")  # цена лота
price_proc = find_all_td_align[-1].text.split(",")[0]  # процент от цены ля задатка
deposit = int(lot_price) / 100 * int(price_proc)



# aray = [
#     efrsb_num,
#     efrsb_publice,
#     obligator,
#     adres_of_oblig,
#     arbitor_man,
#     snils_arbit_man,
#     inn_arbit_man,
#     obligator_inn,
#     elect_plase,
#     proces,
#     opn_clos,
#     lot_namber,
#     lot_name,
#     lot_price,
#     price_proc,
#     deposit
# ]


variables = {
    "${DATE}": todayis,  # дата создания договора
    "${CLIENT_NAME}": "Тазылисламов Руслан Робертович",  # имя клиента
    "${PASPORT_SERIA}": "8008",  # СЕРИЯ ПАСПОРТА клиента
    "${PASPORT_NUMBER}": "605164",  # НОМЕР ПАСПОРТА клиента
    "${PASPORT_HOME}": "Отделением УФМС России по республике Башкортостан в гор. Таймазы",  # орган выдавший паспорт ПАСПОРТА клиента
    "${PASPORT_DATE}": "25.08.2008",  # дата выдачи ПаСПОРТА клиента
    "${PASPORT_CODE}": "020-025",  # код подразделения ПАСПОРТА клиента
    "${REGISTER}": "г. Омск ул. Рокосовсткого дом№ 32 кв. 254",  # Прописка клиента
    "${POST_INDEX}": "644073",  # Почтовый индекс
    "${INN}": "024400220096",  # ИНН клиента
    "${SNILS}": "133-217-431 17",  # СНИЛС клиента
    "${CITY}": "г. Волгоград",  # город создания договора
    "${BANK_NAME}": 'ФИЛИАЛ "ЦЕНТРАЛЬНЫЙ" ПАО "СОВКОМБАНК"',  # нименование банка
    "${BANK_BIK}": "045004763",  # БИК банка участника
    "${BANK_INN}": "4401116480",  # ИНН банка участника
    "${BANK_KPP}": "544543001",  # КПП банка участника
    "${BANK_RS_NUMBER}": "40817810750168739672",  # Р/С НОМЕР участника
    "${BANK_KS_NUMBER}": "30101810150040000763",  # К/С НОМЕР участника
    "${CLIENT_MAIL}": "pl128@bk.ru",  # Электронная почта клиента Учасника
    "${CLIENT_PHONE}": "+79609952665",  # номер телефона Учасника
    "${EFRSB_NUMBER}": efrsb_num,  # Номер публикации в ЕФРСБ
    "${EFRSB_PUBLIC_DATE}": efrsb_publice,  # Дата публикации в ЕФРСБ
    "${OBLIGOR_NAME}": obligator,  # фио должника
    "${PLASE_OBLIGOR}": adres_of_oblig,  # Место нахождения должника
    "${INN_OBLIGOR}": obligator_inn,  # ИНН должника
    "${SNIL_OGRN_OBLIGOR}": f"{obligator_snils}",  # Снилс или ОГРН долника ввод включая слово "Снилс" или "ОГРН"
    "${ARBITRATION_MANAGER}": arbitor_man,  # ФИО Арбитражного управляющео
    "${INN_CNILS_arbitration_manager}": f"(ИНН: {inn_arbit_man} СНИЛС: {snils_arbit_man}",  # инн снилс арбитражного упровляющего
    "${Sro_Arbitration}": 'Союз арбитражных управляющих "Возрождение" (ИНН 7718748282,  ОГРН 1127799026486)',  # наименование СРО АУ
    "${PROCES}": proces,  # Тип проведения торгов
    "${OPCLOSE}": opn_clos,  # Форма подачи ценовых предложений
    "${ELECTONIC_PLASE}": elect_plase,  # Этп проведения
    "${THE_PROC_CODE}": "182279",  # Код процедуры
    "${LOT_NAME}": f"{lot_namber} - {lot_name}",  # Наименование и номер лота
    "${DATA_AUCKCIONA}": "_______ - ___________",  # дата провдения
    "${LOT_PRICE}": lot_price,  # цена лота
    "${PERCENT_LOT_PRICE}": price_proc,  # процент от цены лота
    "${DEPOSIT}": deposit,  # Размер задатка
    "${OFEER_PRICE}": "__________________",  # цена предложения
}

for key,value in variables.items():
    print(value)
# if __name__ == '__main__':
#     main()

# print(variables)
