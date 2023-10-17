# doc = DocxTemplate("Agent_dogovor_template.docx")
# doc.render(data_from_pars)
# doc.save(f'Агентский договор лот№{lot_namber}.docx')

# if proces == "Открытый аукцион":
#     doc = DocxTemplate("Zayavka_auction.docx")
#     doc.render(data_from_pars)
#     doc.save(f'заявка аукцион лот№{lot_namber}.docx')
# if proces == "Публичное предложение": 
#     doc = DocxTemplate("Zayavka_pablic.docx")
#     doc.render(data_from_pars)
#     doc.save(f'заявка публичка лот№{lot_namber}.docx')

ans=True
while ans:
    print (""""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    """")