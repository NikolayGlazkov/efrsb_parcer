import efrsb_parser
import datetime
from petrovich.main import Petrovich



def sklonenie_name(name: str, declination: str):  # определение пола по отчеству
    p = Petrovich()

    if name.split(" ")[-1][-2:] == "ич" or name.split(" ")[-1][-2:] == "лы":
        gender_arbit = "male"
    elif (
        name.split(" ")[-1][-2:] == "на"
        or name.split(" ")[-1][-2:] == "зы"
        or name.split(" ")[0][-2:] == "ва"
    ):
        gender_arbit = "female"
    di_decl = {
        "GENITIVE": 0,
        "DATIVE": 1,
        "ACCUSATIVE": 2,
        "INSTRUMENTAL": 3,
        "PREPOSITIONAL": 4,
    }
    decl = di_decl[declination]
    lastname_s = p.lastname(name.split(" ")[0], decl, gender_arbit)
    name_s = p.firstname(name.split(" ")[1], decl, gender_arbit)
    middlename_s = p.middlename(name.split(" ")[2], decl, gender_arbit)

    recipient = (
        f"{lastname_s} {name_s} {middlename_s}"  # имя в дательном падеже для шапки заяв
    )
    return recipient


"""легковой фиат"""
# url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=5CAF3F3B0FAB4776A36F5BF6A9C12926"
"""ООО должник"""
# url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=723F95257A3A4A1DAC1035AEF2017775"
""""""
url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=4D7C894B4B3D4092B71A2314A909DD27"

# # print(efrsb_parser.data_lot_tabel(url))
# # print(efrsb_parser.make_content_dict(url))
dikt_temp = {
    "1": {
        "Описание": "Борона дисковая БД-6*4 ПК ШКС, 2020 года выпуска, заводской номер: 2036",
        "Начальная цена, руб": "774 000,00",
        "Шаг": "5,00 %",
        "Задаток": "5,00 %",
    },
    "2": {
        "Описание": "Культиватор предпосевной КПС-4,7, 2020 года выпуска, заводской номер 2215",
        "Начальная цена, руб": "135 000,00",
        "Шаг": "5,00 %",
        "Задаток": "5,00 %",
    },
    "3": {
        "Описание": "Сеялка зерновая, прицепная U-drill 6М Plus, 2016 года выпуска,\nзаводской/серийный номер: ACPNDxx65718",
        "Начальная цена, руб": "5 832 747,00",
        "Шаг": "5,00 %",
        "Задаток": "5,00 %",
    },
}

dict_two = {
    "№ сообщения": "12548256",
    "Дата публикации": "26.09.2023",
    "Наименование должника": 'ООО "ФАС"',
    "Адрес": "355045, КРАЙ СТАВРОПОЛЬСКИЙ, ГОРОД СТАВРОПОЛЬ, УЛИЦА ПИРОГОВА, ДОМ 44, ОФИС 4",
    "ОГРН": "1142651003780",
    "ИНН": "2635827421",
    "Арбитражный управляющий": "Стексов Алексей Васильевич (ИНН 581701327480,  СНИЛС 142-206-521 10)",
    "Адрес для корреспонденции": "129515, г. Москва, а/я 91",
    "СРО АУ": 'Союз арбитражных управляющих "Возрождение" (ИНН 7718748282,  ОГРН 1127799026486)',
    "Адрес СРО АУ": "107078, г Москва, г Москва, ул. Садовая-Черногрязская , дом 8, стр.1, офис 304",
    "Вид торгов": "Открытый аукцион",
    "Дата и время торгов": "15.11.2023 12:00 (Московское время МСК)",
    "Форма подачи предложения о цене": "Открытая",
    "Место проведения": "Центр дистанционных торгов",
}

"""присвоение имени должника в результативный список"""
# # Родительный
#     GENITIVE = 0
#     # Дательный
#     DATIVE = 1
#     # Винительный
#     ACCUSATIVE = 2
#     # Творительный
#     INSTRUMENTAL = 3
#     # Предложный
#     PREPOSITIONAL = 4


if len(dict_two["ИНН"]) == 12:
    name_of_obligator = dict_two["ФИО должника"]
    obligator_rad = sklonenie_name(dict_two["ФИО должника"], "GENITIVE")
elif len(dict_two["ИНН"]) == 10:
    name_of_obligator = dict_two["Наименование должника"]
    obligator_rad = dict_two["Наименование должника"]
    obligator_snils = f"ОГРН {dict_two['ОГРН']}"
else:
    name_of_obligator = None  # Вы можете установить значение по умолчанию или обработать другим способом


# if
variables = {
    "DATE": datetime.date.today().strftime("%d.%m.%Y"),  # дата создания договора
    "EFRS_NUM": dict_two["№ сообщения"],  # Номер публикации в ЕФРСБ
    "EFRSB_PUB_DAT": dict_two["Дата публикации"],  # Дата публикации в ЕФРСБ
    "OBLIGOR_NAME": name_of_obligator,  # фио должника
    "OBL_MAN_IN_RAD": obligator_rad,  # фио должника в радительном
    "PLASE_OBLIGOR": dict_two["Адрес"],  # Место нахождения должника
    "INN_OBLIGOR": dict_two["ИНН"],  # ИНН должника
    "SNIL_OGRN_OBLIGOR": obligator_snils,  # Снилс или ОГРН долника ввод включая слово "Снилс" или "ОГРН"
    # "opn_clos_an": opn_clos_an,
    # "arb_man_name": arbitor_man,  # ФИО Арбитражного управляющео
    # "AR_MAN_IN_DAT": recipient,  # ФИО арбитр в склоеннии
    # "INN_CNI_arbit_manager": f"ИНН: {inn_arbit_man} СНИЛС: {snils_arbit_man}",  # инн снилс арбитражного упровляющего
    # "Sro_Arbitration": sro_name,  # наименование СРО АУ
    # "PROCES": proces,  # Тип проведения торгов
    # "TYPE_OF_BID": type_of_bidding,  # склонение типа проведения торгов
    # "OPCLOSE": opn_clos,  # Форма подачи ценовых предложений
    # "ELECTONIC_PLASE": elect_plase,  # Этп проведения
    # "THE_P_COD": "182279",  # Код процедуры
    # "lot_namber": lot_namber,
    # "LOT_NAME": lot_name,  # Наименование и номер лота
    # "DATA_AUCKCIONA": acsion_date,  # дата провдения
    # "LOT_PRICE": lot_price,  # цена лота
    # "PERCENT_LOT_PRICE": price_proc,  # процент от цены лота
    # "DEPOSIT": deposit,  # Размер задатка
    # "opn_clos_skl": opn_clos_skl,
    # "OFEER_PRICE": "__________________",  # цена предложения
}
for key,value in variables.items():
    print(key,value)