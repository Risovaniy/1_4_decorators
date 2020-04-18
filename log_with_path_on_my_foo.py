import json
import time


def logs_with_path(path):
    def foo_logs(total_foo):
        file_path = path
        def log_foo(*args, **kwargs):
            nonlocal file_path
            local_time = time.localtime()
            date_today = time.strftime("%d.%m.%Y", local_time)
            time_start = time.strftime("%H:%M:%S", local_time)
            run_foo = total_foo(*args, **kwargs)
            logs = {'date': date_today, 'start': time_start, 'name':total_foo.__name__, 'args': args,
                    'kwargs': kwargs, 'return': run_foo}
            with open(file_path, 'a') as f:
                json.dump(logs, f, indent=2)
            return run_foo

        return log_foo

    return foo_logs


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
       '1': ['2207 876234', '11-2', '5455 028765'],
       '2': ['10006', '5400 028765', '5455 002299'],
       '3': []
      }


programme = True

@logs_with_path('log_file2.json')
def people_owner(docs):
    """Show an owner the doc"""

    check_p = False
    while check_p == False:
        doc_number = input('Введите номер документа: \n')
        # check_doc_catalog(doc_number, docs)
        for doc in docs:
            if doc['number'] == doc_number:
                if doc["name"] == '':
                    new_people = input(f'Документ {doc_number} никому не принадлежит\n'
                                           f'Введите имя и фамилию владельца через пробел\n')
                    docx[doc]["name"] = new_people
                else:
                    print(f'{doc["name"]} владелец документа №{doc_number}\n')
                check_p = True
                break
        if check_p == False:
            new_command = input(f'Документ номер {doc_number} не был найден\n'
                                    'Нажмите Enter для повторного ввода номера документа\n'
                                    'q – вернуться к глобальному выбору команд\n')
            if new_command == 'q': return 0


def shelf(dirt, docs):
    doc_number = input('Введите номер документа\n')
    for shelf in dirt:
        for doc in dirt[shelf]:
            if doc == doc_number:
                print(f'Документ {doc_number} находится на полке №{shelf}\n')
                return 0
    print(f'Документ номер {doc_number} не был найден\n')


def check_doc_catalog(doc_number, docs):
    """Checking the presence of a document in the catalog."""
    check = False
    for doc in docs:
        if doc['number'] == doc_number:
            check = True
    if check == False:
        new_command = input(f'Документ номер {doc_number} не был найден\n'
                                 'Нажмите Enter для повторного ввода номера документа\n'
                                 'q – вернуться к глобальному выбору команд\n')
        if new_command == 'q': return


def list_of_docs(docs):
    for doc in docs:
        for parameter in doc.values():
            print(parameter, end=' ')
        print('\n')


def add(docs, dirt):
    doc_type = input('Введите тип документа:\n')
    doc_number= input('Введите номер документа:\n')
    doc_name = input('Введите имя владельца документа:\n')
    new_doc = {"type":doc_type, "number":doc_number, "name":doc_name}

    shelf = input('Введите номер полки:\n')

    while not check_shelf(shelf):
        shelf = input(f'Полка №{shelf} не найдена\n'
                          'Введите номер полки повторно\n'
                          'Введите "q" для отмены добавления документа\n')
    if check_shelf(shelf):
        docs.append(new_doc)
        dirt[shelf].append(new_doc["number"])
        print(f'Докумен:\n'
              f'{doc_type}\n'
              f'{doc_number}\n'
              f'{doc_name}\n'
              f'Успешно добавлен на полку №{shelf}\n')
        return
    print('Добавление документа прерванно\n')



def check_shelf(number_shelf):
    for shelf in directories:
        if shelf == number_shelf:
            return True
    return False


def quit():
    print('Вы вышли из каталога')
    exit()


def main(docs=documents, dirt=directories):
    command = input('Введите комманду: \n'
                        'p – вывести на экран имя владельца документа\n'
                        'l – вывести данные всех документов\n'
                        's – вывести номера полки на которой находится искомый документ\n'
                        'a – добавить новый документ в каталог\n'
                        'q – закрыть программу\n\n')
    if command == 'p':
        people_owner(docs)
    elif command == 'l':
        list_of_docs(docs)
    elif command == 's':
        shelf(dirt, docs)
    elif command == 'a':
        add(docs, dirt)
    elif command == 'q':
        quit()
    else:
        new_command = input('Некорректная команда.\n'
            'Нажмите Enter для повторного ввода команды\n')


while True:
    main()
