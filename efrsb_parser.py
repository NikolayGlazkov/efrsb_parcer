from selenium import webdriver
from selenium.webdriver.common.by import By



def data_lot_tabel(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    table = driver.find_element(By.CLASS_NAME, "lotInfo")  # таблица с инфо о лоте
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    array_temp = []
    for row in rows:
        array = []
        cells = row.find_elements(By.TAG_NAME, "td")
        for cell in cells:
            array.append(cell.text)
        if array:  # Проверка, что список array не пустой
            array_temp.append(array)

    result_dict = {}
    current_key = None

    for item in array_temp:
        if item:
            if item[0].isdigit():
                current_key = item[0]
                result_dict[current_key] = {
                    "Описание": item[1],
                    "Начальная цена, руб": item[2],
                    "Шаг": item[3],
                    "Задаток": item[4],
                }
        elif current_key:
            result_dict[current_key]["Описание"] += "\n" + item[0]
    driver.quit()
    return result_dict

def make_content_dict(url):

    driver = webdriver.Chrome()
    driver.get(url)

    driver.implicitly_wait(10)

    elements_with_primary_class = driver.find_elements(By.CLASS_NAME, "primary")

    array_temp = []
    respons_text = [
        "№ сообщения",
        "Дата публикации",
        "ФИО должника",
        "Наименование должника",
        "Место жительства",
        "Адрес",
        "ОГРН",
        "ИНН",
        "СНИЛС",
        "Арбитражный управляющий",
        "СРО АУ",
        "Вид торгов",
        "Дата и время торгов",
        "Форма подачи предложения о цене",
        "Место проведения",
    ]
    for element in elements_with_primary_class:
        for text in respons_text:
            if text in element.text:
                td_elements = element.find_elements(By.XPATH, ".//ancestor::tr[1]//td")
                aray = []
                for td in td_elements:
                    aray.append(td.text)
                array_temp.append(aray)
                my_dict = {item[0]: item[1] for item in array_temp}

    driver.quit()
    return my_dict



    


