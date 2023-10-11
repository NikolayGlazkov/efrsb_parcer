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
            doc.save(f'заявка публичка лот№{lot_namber}.docx')
