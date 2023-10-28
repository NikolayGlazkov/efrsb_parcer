from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate
import made_resu_dickt

def made_docx_file(data_from_pars:dict,lot_namber,filename:str): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate(filename)
        doc.render(data_from_pars)
        if filename == "Zayavka_auction.docx":
            doc.save(f'Заявка для аукциона лот№{lot_namber}.docx')
        elif filename == "Zayavka_pablic.docx":
             doc.save(f'Заявка для публички лот№{lot_namber}.docx')
        elif filename == "Agent_dogovor.docx":
            doc.save(f'Агентский договр лот№{lot_namber}.docx')


"""ООО должник"""
url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=4D7C894B4B3D4092B71A2314A909DD27"
lot_namber = "1"

data_from_pars = made_resu_dickt.make_result_dikt(url=url,lot_num=lot_namber) 

made_docx_file(data_from_pars,lot_namber,"Agent_dogovor.docx")
if data_from_pars["PROCES"] == "Открытый аукцион":
    made_docx_file(data_from_pars,lot_namber,"Zayavka_auction.docx")
if data_from_pars["PROCES"] == "Публичное предложение": 
    made_docx_file(data_from_pars,lot_namber,"Zayavka_pablic.docx")
if data_from_pars["PROCES"] == "Закрытый аукцион":
    made_docx_file(data_from_pars,lot_namber,"Zayavka_auction.docx")

