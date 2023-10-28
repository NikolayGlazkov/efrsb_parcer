def ClientInfo():
    klient_info = {
        "CITY": "г. Волгоград",  # город создания договора
        "CL_NAME": "Яндиев Магомед Бесланович",  # имя клиента
        "CL_NAM_skr": "Яндиев М. Б.",
        "Cl_name_in_":"Яндиева Магомеда Беслановича",
        "PASPORT_SERIA": "2603",  # СЕРИЯ ПАСПОРТА клиента
        "PASPORT_NUMBER": "109274",  # НОМЕР ПАСПОРТА клиента
        "PASPORT_HOME": "Отделом Внутренних дел Малгобекского района республиуи Ингушетия",  # орган выдавший паспорт ПАСПОРТА клиента
        "PASPORT_DATE": "27.09.2006",  # дата выдачи ПаСПОРТА клиента
        "PASPORT_CODE": "062-006",  # код подразделения ПАСПОРТА клиента
        "REGISTER": "Малгобекский р-н, республика Ингушетия с. Инарки ул. 50 лет Октября дом№11",  # Прописка клиента
        "POST_INDEX": "386333",  # Почтовый индекс
        "INN": "060108349691",  # ИНН клиента
        "SNILS": "169-867-865 65",  # СНИЛС клиента
        "BANK_NAME": "СТАВРОПОЛЬСКОЕ ОТДЕЛЕНИЕ N5230 ПАО СБЕРБАНК",  # нименование банка
        "BANK_BIK": "040702615",  # БИК банка участника
        "BANK_INN": "7707083893",  # ИНН банка участника
        "BANK_KPP": "060602001",  # КПП банка участника
        "BANK_RS_NUMBER": "40817810460353238203",  # Р/С НОМЕР участника
        "BANK_KS_NUMBER": "30101810907020000615",  # К/С НОМЕР участника
        "CLIENT_MAIL": "yandiev080986@mail.ru",  # Электронная почта клиента Учасника
        "CLIENT_PHONE": "+7 928 734-02-10",  # номер телефона Учасника
        "THE_P_COD": "189721",
        "OFEER_PRICE": "_____"  # цена предложения
    }  # Код процедуры с площадки
    return klient_info


import sqlite3

class ClientInfoDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS ClientData (
                CLIENT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                CITY TEXT,
                CL_NAME TEXT,
                CL_NAM_skr TEXT,
                ...  # Остальные поля таблицы здесь
                OFEER_PRICE TEXT
            )
        ''')
        self.conn.commit()

    def insert_client_info(self, klient_info):
        columns = ', '.join(klient_info.keys())
        placeholders = ', '.join(['?'] * len(klient_info))
        values = tuple(klient_info.values())
        self.cursor.execute(f"INSERT INTO ClientData ({columns}) VALUES ({placeholders})", values)
        self.conn.commit()

    def get_client_info(self, client_id):
        self.cursor.execute("SELECT * FROM ClientData WHERE CLIENT_ID=?", (client_id,))
        return self.cursor.fetchone()

    # Другие методы для работы с базой данных, например, обновление данных, удаление клиента и т.д.

    def close_connection(self):
        self.conn.close()

# Пример использования класса ClientInfoDB
if __name__ == "__main__":
    client_db = ClientInfoDB('client_info.db')

    klient_info = {
        "CITY": "г. Волгоград",
        "CL_NAME": "Яндиев Магомед Бесланович",
        # ... Остальные данные
        "OFEER_PRICE": "_____"
    }

    # Добавление информации о клиенте в базу данных
    client_db.insert_client_info(klient_info)

    # Получение информации о клиенте из базы данных
    client_id = 1  # Предположим, что это ID клиента
    client_data = client_db.get_client_info(client_id)
    print("Данные клиента:", client_data)

    client_db.close_connection()
