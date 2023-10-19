from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate
import made_resu_dickt

def made_docx_file(data_from_pars:dict,lot_namber,filename:str): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate(filename)
        doc.render(data_from_pars)
        doc.save(f'{filename} лот№{lot_namber}.docx')



"""ООО должник"""
url = "https://old.bankrot.fedresurs.ru/MessageWindow.aspx?ID=DC425B49E55449E685C90FCF652D65BF"

lot_namber = "1"

data_from_pars = made_resu_dickt.make_result_dikt(lot_namber,url=url) 

made_docx_file(data_from_pars,lot_namber,"Agent_dogovor.docx")
if data_from_pars["PROCES"] == "Открытый аукцион":
    made_docx_file(data_from_pars,lot_namber,"Zayavka_auction.docx")
if data_from_pars["PROCES"] == "Публичное предложение": 
    made_docx_file(data_from_pars,lot_namber,"Zayavka_pablic.docx")


