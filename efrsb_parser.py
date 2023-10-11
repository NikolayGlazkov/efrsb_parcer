import datetime
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from petrovich.main import Petrovich
from petrovich.enums import Case, Gender
####
# часть того что отвечает за док 
from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate


def made_docx_file(data_from_pars:dict,proces:str,lot_namber): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate("Agent_dogovor_template.docx")
        doc.render(data_from_pars)
        doc.save(f'Агентский договор лот№{lot_namber}.docx')

        if proces == "Открытый аукцион":
            doc = DocxTemplate("Zayavka_auction.docx")
            doc.render(data_from_pars)
            doc.save(f'заявка аукцион лот№{lot_namber}.docx')
        if proces == "Публичное предложение": 
            doc = DocxTemplate("Zayavka_pablic.docx")
            doc.render(data_from_pars)
            doc.save(f'заявка аукцион лот№{lot_namber}.docx')

def gender_find(last_name: str): # определение пола по отчеству
    
    if last_name[-2:] == "ич" or last_name[-2:] == "лы":
        return "male"
    elif last_name[-2:] == "на" or last_name[-2:] == "зы" or last_name[-2:] == "ва":
        return "female"

def make_dict_from_pars(url:str):
    p = Petrovich()

    driver = webdriver.Chrome("")
    driver.get(url)
    html_code = driver.page_source  # содержимое страницы
    soup = bs(html_code, "html.parser")

    oll_info = soup.find_all(class_="even")
    oll_info1 = soup.find_all(class_="odd")
    oll_info2 = soup.find_all(class_="primary")
    oll_info3 = soup.find_all(class_="lotInfo")
    find_all_td_align = soup.find_all("td", align="right")
    oll_info4 = soup.find_all("tr", class_="even")



    # print(*oll_info[6].text.split()) # @mail орбитражного
    efrsb_num = oll_info[0].text.split()[-1]  # номер публикации в ефрсб
    efrsb_publice = oll_info1[0].text.split()[-1]  # дата публикации в ефрсб
    todayis = datetime.date.today().strftime("%d.%m.%Y")  # дата сегодня
    obligator = " ".join(oll_info[1].text.split()[-3:])  # ФИО должника
    adres_of_oblig = " ".join(oll_info1[2].text.split()[2:])  # место жительства
    arbitor_man = " ".join(oll_info[5].text.split()[2:-5])  # Фио Арбитражного упр.
    obligator_snils = " ".join(oll_info1[3].text.split()[1:])  # снилс Должника
    inn_arbit_man = " ".join(
        oll_info[5].text.split()[-4:-3]
    )  # ИНН арбитражного упровляющего
    snils_arbit_man = " ".join(oll_info[5].text.split()[-2:-1])  # SNILS арбитражного
    obligator_inn = " ".join(oll_info[3].text.split()[-1]).replace(" ", "")  # инн должника
    elect_plase = oll_info[-1].text[16:]  # площадка проведения
    proces = oll_info[-4].text[10:]  # тип процедуры
    opn_clos = oll_info1[-2].text.split()[-1]  # метод проведения торгов откр. закр.
    lot_namber = oll_info1[-1].text[0]  # номер лота
    lot_name = oll_info1[-1].text  #  имя лота
    lot_price = str(find_all_td_align[-3].text.split(",")[0]).replace(" ", "")  # цена лота
    price_proc = find_all_td_align[-1].text.split(",")[0]  # процент от цены ля задатка
    deposit = int(lot_price) / 100 * int(price_proc)
    sro_name = " ".join(oll_info4[-5].text.split())  # имя сро
    acsion_date = oll_info4[-2].text[19:-10] # дата проведения 
    
    print(opn_clos_an)

    if proces == "Открытый аукцион":
        type_of_bidding = "открытого аукциона"  # Склоенние формы проедения перменная
    elif proces == "Публичное предложение":
        type_of_bidding = "публичного предложения"


    if opn_clos == "Открытая":
        opn_clos_skl = "открытой" 
        opn_clos_an = "открытых"
    elif opn_clos == "Закрытая":
        opn_clos_skl = "закрытой"
        opn_clos_an = "закрытых"

    #     Родительный
    #     GENITIVE = 0
    #     # Дательный
    #     DATIVE = 1
    #     # Винительный
    #     ACCUSATIVE = 2
    #     # Творительный
    #     INSTRUMENTAL = 3
    #     # Предложный
    #     PREPOSITIONAL = 4

    """ обращение к арбитражному в дательном падеже """
    # gender_arbit = gender_find(arbitor_man.split()[2])
    # arbitor_lastname_dati = p.lastname(arbitor_man.split()[0], Case.DATIVE, gender_arbit)
    # arbitor_name_dati = p.firstname(arbitor_man.split()[1], Case.DATIVE, gender_arbit)
    # arbitor_middlename_dati = p.middlename(arbitor_man.split()[2], Case.DATIVE, gender_arbit)
    # арбитражный в дательном
    # recipient = f"{arbitor_lastname_dati} {arbitor_name_dati} {arbitor_middlename_dati}"  # имя в дательном падеже для шапки заявки


    """обрашение к должнику в Родительнном падеже"""
    # gender_obligator = gender_find(obligator.split()[2])
    # obligator_lastname_rad = p.lastname(obligator.split()[0], Case.GENITIVE, gender_obligator)
    # obligator_name_rad = p.firstname(obligator.split()[1], Case.GENITIVE, gender_obligator)
    # obligator_middlename_rad = p.middlename(obligator.split()[2], Case.GENITIVE, gender_obligator)
    # должник в радительном
    # obligator_rad = f"{obligator_lastname_rad} {obligator_name_rad} {obligator_middlename_rad}"




    variables = {
        "DATE": todayis,  # дата создания договора
        "CL_NAME": "ООО «ДОРИНВЕСТ»",  # имя клиента
        "CL_NAM_skr" :"",
        "PASPORT_SERIA":'',  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER" : "",  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "Волгоградская область, район Городищенский, р.п. Городище, ул. Пушкина, д. № 5",  # Прописка клиента
        "POST_INDEX": "403002",  # Почтовый индекс
        "INN": "3444278148",  # ИНН клиента
        "SNILS": "1223400007357",  # СНИЛС клиента
        "CITY": "г. Волгоград",  # город создания договора
        "BANK_NAME": 'ФИЛИАЛ «РОСТОВСКИЙ» АО «АЛЬФА-БАНК»',  # нименование банка
        "BANK_BIK": "046015207",  # БИК банка участника
        "BANK_INN": "",  # ИНН банка участника
        "BANK_KPP": "КПП",  # КПП банка участника
        "BANK_RS_NUMBER": "40702810126010007640",  # Р/С НОМЕР участника
        "BANK_KS_NUMBER": "30101810500000000207",  # К/С НОМЕР участника
        "CLIENT_MAIL": "dorinvest2022@gmail.com",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+7 927 534-44-55",  # номер телефона Учасника
        
        "EFRS_NUM": efrsb_num,  # Номер публикации в ЕФРСБ
        "EFRSB_PUB_DAT": efrsb_publice,  # Дата публикации в ЕФРСБ
        "OBLIGOR_NAME": obligator,  # фио должника
        "OBL_MAN_IN_RAD": "", #obligator_rad, # фио должника в радительном
        "PLASE_OBLIGOR": adres_of_oblig,  # Место нахождения должника
        "INN_OBLIGOR": obligator_inn,  # ИНН должника
        "SNIL_OGRN_OBLIGOR": obligator_snils,  # Снилс или ОГРН долника ввод включая слово "Снилс" или "ОГРН"
        "opn_clos_an": opn_clos,#opn_clos_an,
        "arb_man_name": arbitor_man,  # ФИО Арбитражного управляющео
        "AR_MAN_IN_DAT": "", #recipient,  # ФИО арбитр в склоеннии
        "INN_CNI_arbit_manager": f"ИНН: {inn_arbit_man} СНИЛС: {snils_arbit_man}",  # инн снилс арбитражного упровляющего
        "Sro_Arbitration": sro_name,  # наименование СРО АУ
        "PROCES": proces,  # Тип проведения торгов
        "TYPE_OF_BID": type_of_bidding,  # склонение типа проведения торгов
        "OPCLOSE": opn_clos,  # Форма подачи ценовых предложений
        "ELECTONIC_PLASE": elect_plase,  # Этп проведения
        "THE_P_COD": "182279",  # Код процедуры
        "lot_namber":lot_namber,
        "LOT_NAME": lot_name,  # Наименование и номер лота
        "DATA_AUCKCIONA": acsion_date,  # дата провдения
        "LOT_PRICE": lot_price,  # цена лота
        "PERCENT_LOT_PRICE": price_proc,  # процент от цены лота
        "DEPOSIT": deposit,  # Размер задатка
        "opn_clos_skl":opn_clos_skl,
        "OFEER_PRICE": "__________________",  # цена предложения
    }
    
    return variables

# print(proces)
url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=723F95257A3A4A1DAC1035AEF2017775"
content = make_dict_from_pars(url)


made_docx_file(content,content["PROCES"],content["lot_namber"])

