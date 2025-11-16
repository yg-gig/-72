print()
bool_file = 1
with open('hello.txt', 'a+') as file:
    books = [

    ]

    book_num = 1


    def append_book():
        global book_num,books
        try:

            new_book={
                "book":input("Название книги: "),
                "year":int(input("Год издания: ")),
                "number":book_num}
            book_num = + 1
            books.append(new_book)
        except ValueError:
            print('чё сЛепОй')


    def delete_book():
        global books
        if not books:
            print("Список книг пуст!")
            return
        book_num = input("Введите номер книгу или номер для удаления: ")
        try:
            book_num = int(book_num)
            book_found = False

            for i, book in enumerate(books):
                if book['number'] == book_num:
                    books.pop(i)
                    print(f"Книга  удалена!")
                    book_found = True
                    break

            if not book_found:
                print("Книга с таким номером не найдена!")
                return

        except ValueError:
            book_found = False
            for i, book in enumerate(books):
                if book['title'].lower() == book_num.lower():
                    deleted_book = book.pop(i)
                    print(f"Книга '{deleted_book['title']}'сожжена")
                    book_found = True
                    break
            if not book_found:
                print("Книг не видел")
                return

    def book_clear():
        books.clear()
        file.truncate(0)


    def search_book():
        print("НЕ умный поиск книги")
        print("1 - Поиск по названию или году")
        print("2 - Поиск по номеру")

        user_choice = input("Выберите что когда или какого искать: ").strip()

        if user_choice == '1':

            user_search = input("Введите название книги или дату издания: ").strip()
            found_books = []

            for book in books:

                if user_search.lower() in book['book'].lower():
                    found_books.append(book)

                elif int(user_search) == book['year']:
                    found_books.append(book)

            if found_books:
                print("\nНайденные книги:")
                for book in found_books:
                    print(f"Номер: {book['number']}, Название: {book['book']}, когда родилась {book['year']}")
            else:
                print("Книги не найдены!")

        elif user_choice == '2':

            try:
                user_search = int(input("Введите номер книги: "))
                found_books = []

                for book in books:
                    if book['number'] == user_search:
                        found_books.append(book)
                        break

                if found_books:
                    print("\nНайденная книга:")
                    for book in found_books:
                        print(f"Номер: {book['number']}, Название: {book['book']}, когда родилась {book['year']}")
                else:
                    print("Книга с таким номером не найдена!")

            except ValueError:
                print("Ошибка: номер должен быть числом!")

        else:
            print("Неверный выбор!")
    def replacement():
        replacement_name= input()
        replacement_book = input()
        for book in books:
            if replacement_name == book["book"]:
                book['book'] = replacement_book
    while bool_file == 1:
        try:
            i_book = 0
            user_chose = int(input('ведите номер функции'))
            if user_chose == 1:
                print(append_book())
            if user_chose == 2:
                delete_book()
            if user_chose == 3:
                book_clear()
            if user_chose == 4:
                search_book()
            if user_chose== 5:
                replacement()
            if user_chose == 6:
                file.seek(0)
                content = file.read()
                print(content)
        except ValueError:
            print('иди плачь в подушку')
        finally:
            file.truncate(0)
            file.write(str(books))
