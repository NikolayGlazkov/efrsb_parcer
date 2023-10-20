import efrsb_parser
import About_client_info
import datetime
from petrovich.main import Petrovich
import re



"""мы делаем результотирующий список из двух списков импортируемых из файла efrsb_parser"""


def sklonenie_name(
    name: str, declination: str
):  # определение пола по отчеству, нужно указывать падеж

    #   переменная = sklonenie_name(ФИО должника, "Склонение")
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

    p = Petrovich()

    if name.split(" ")[-1][-2:] == "ич" or name.split(" ")[-1][-2:] == "лы":
        gender = "male"
    elif (
        name.split(" ")[-1][-2:] == "на"
        or name.split(" ")[-1][-2:] == "зы"
        or name.split(" ")[0][-2:] == "ва"
    ):
        gender = "female"
    di_decl = {
        "GENITIVE": 0,
        "DATIVE": 1,
        "ACCUSATIVE": 2,
        "INSTRUMENTAL": 3,
        "PREPOSITIONAL": 4,
    }
    decl = di_decl[declination]
    lastname_s = p.lastname(name.split(" ")[0], decl, gender)
    name_s = p.firstname(name.split(" ")[1], decl, gender)
    middlename_s = p.middlename(name.split(" ")[2], decl, gender)

    recipient = (
        f"{lastname_s} {name_s} {middlename_s}"  # имя в дательном падеже для шапки заяв
    )
    return recipient


def make_result_dikt(url:str,lot_num = "1"):
    dikt_table = efrsb_parser.data_lot_tabel(url)
    dict_two = efrsb_parser.make_content_dict(url)

    clieInf = About_client_info.ClientInfo()
    if len(dict_two["ИНН"]) == 12:
        name_of_obligator = dict_two["ФИО должника"]
        obligator_rad = sklonenie_name(dict_two["ФИО должника"], "GENITIVE")
        ob_snils_ogrn = f"СНИЛС {dict_two['СНИЛС']}"
        adres = dict_two["Место жительства"]
    elif len(dict_two["ИНН"]) == 10:
        name_of_obligator = dict_two["Наименование должника"]
        obligator_rad = dict_two["Наименование должника"]
        ob_snils_ogrn = f"ОГРН {dict_two['ОГРН']}"
        adres = dict_two["Адрес"]
    else:
        name_of_obligator = None  # Вы можете установить значение по умолчанию или обработать другим способом

    if dict_two["Вид торгов"] == "Открытый аукцион":
        type_of_bidding = "открытого аукциона"  # Склоенние формы проедения перменная
    elif dict_two["Вид торгов"] == "Публичное предложение":
        type_of_bidding = "публичного предложения"


    if dict_two["Форма подачи предложения о цене"] == "Открытая":
        opn_clos_skl = "открытой"
        opn_clos_an = "открытых"
    elif dict_two["Форма подачи предложения о цене"] == "Закрытая":
        opn_clos_skl = "закрытой"
        opn_clos_an = "закрытых"
    name_arbitr = " ".join(re.split(r'\s+',dict_two["Арбитражный управляющий"])[:3])
    INN_CNI_arbit_manager = " ".join(re.split(r'\s+',dict_two["Арбитражный управляющий"])[3:])

    acsion_date = dict_two["Дата и время торгов"].split()[0]


    lot_price = int(dikt_table[lot_num]["Начальная цена, руб"].split(",")[0].replace(" ", ""))

    percent_price = int(dikt_table[lot_num]["Задаток"].split(",")[0])
    zadatok = lot_price / 100 * percent_price
    lot_info = {
        "DATE": datetime.date.today().strftime("%d.%m.%Y"),  # дата создания договора
        "EFRS_NUM": dict_two["№ сообщения"],  # Номер публикации в ЕФРСБ
        "EFRSB_PUB_DAT": dict_two["Дата публикации"],  # Дата публикации в ЕФРСБ
        "OBLIGOR_NAME": name_of_obligator,  # фио должника
        "OBL_MAN_IN_RAD": obligator_rad,  # фио должника в радительном
        "PLASE_OBLIGOR": adres,  # Место нахождения должника
        "INN_OBLIGOR": dict_two["ИНН"],  # ИНН должника
        "SNIL_OGRN_OBLIGOR": ob_snils_ogrn,  # Снилс или ОГРН долника ввод включая слово "Снилс" или "ОГРН"
        "opn_clos_an": opn_clos_an,
        "opn_clos_skl": opn_clos_skl,
        "arb_man_name": name_arbitr,  # ФИО Арбитражного управляющео
        "AR_MAN_IN_DAT": sklonenie_name(name_arbitr, "DATIVE"),  # ФИО арбитр в склоеннии
        "INN_CNI_arbit_manager": INN_CNI_arbit_manager,  # инн снилс арбитражного упровляющего
        "Sro_Arbitration": dict_two["СРО АУ"],  # наименование СРО АУ
        "PROCES": dict_two["Вид торгов"],  # Тип проведения торгов
        "TYPE_OF_BID": type_of_bidding,  # склонение типа проведения торгов
        "OPCLOSE": dict_two[
            "Форма подачи предложения о цене"
        ],  # Форма подачи ценовых предложений
        "ELECTONIC_PLASE": dict_two["Место проведения"],  # Этп проведения
        "lot_namber": lot_num,
        "LOT_NAME": dikt_table[lot_num]["Описание"],  # Наименование и номер лота
        "DATA_AUCKCIONA": acsion_date,  # дата провдения
        "LOT_PRICE": lot_price,  # цена лота
        "PERCENT_LOT_PRICE": percent_price,  # процент от цены лота
        "DEPOSIT": zadatok  # Размер задатка
        

    }
    
    return clieInf | lot_info
