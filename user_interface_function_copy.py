def get_user_data(users):
    phonebook={}
    print ('Введите информацию о контакте в последовательности Имя, Фамилия, Тел номер, примечание')
    name = input('Enter user name: ')
    surname = input('Enter user surname: ')
    phone_number = input('Enter user phone number: ')
    comment = input('Enter comments: ')
    you_sure = input(f'Хотите скорректировать (yes/no): ').lower()
    if you_sure == 'yes':
        return get_user_data()
    elif you_sure == 'no':
        phonebook.update({'Name': name, 'Surname': surname, 'Phone number': phone_number, 'comments': comment})
        return phonebook
    
# def id_add(users):
#     id = [i for i in range(1,users + 1)]
#     user_data = {'id':id}
#     user_data.update(get_user_data)     
#     print (user_data)
# id_add(10)
