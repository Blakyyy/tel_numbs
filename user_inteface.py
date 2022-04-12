import save_contact as save_con
import read_contact as read_con
import export_XML as e_xml

while True:
    question = input(f'Выберите действие и нажмите: 1- добавить контакт, 2- найти контакт, 3-посмотреть всю книгу, 4 - импортировать тел.книгу')
    if question==1:
        save_con.write_to_file()
    elif question==2:
        read_con.read_exactly(input('Enter surname:').lower())
    elif question==3:
        read_con.read_all_book()  
    elif question==4:
        e_xml.export_to_xml()  
    break



