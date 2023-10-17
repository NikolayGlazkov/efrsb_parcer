from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate


def made_docx_file(data_from_pars:dict,proces:str,lot_namber,filename:str): # словарь мз парсера заходит сюда и взовисимости от типа торгов пишет файл
        doc = DocxTemplate(filename)
        doc.render(data_from_pars)
        doc.save(f'{filename} лот№{lot_namber}.docx')




