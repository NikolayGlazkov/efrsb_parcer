from docx import Document
from docx.shared import Pt
from docxtpl import DocxTemplate


# 


from docxtpl import DocxTemplate
def made_docx_file(context:dict, type_of_proc:str): # взять из словоря
    if type_of_proc == "Открытый аукцион":
        # for i in range(2):
        doc = DocxTemplate("шаблон.docx")
        doc.render(context)
        doc.save("Заявка лот№.docx")


context = { 'ARBITRATION_pizda' : 'gbsdf', 'address1' : 'хуй1', 'участник': 'нечего', 'адрес_участника': 'г. Москва, ул. Полевая, д. 0', 'director': 'И.И. Иванов'}
type_of_proc = "Открытый аукцион"
made_docx_file(context, type_of_proc)