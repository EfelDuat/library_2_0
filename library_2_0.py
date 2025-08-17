# Создаем словарь для хранения книг по жанрам
library = {}

print("*" * 10, "Библиотека", "*" * 10)

while True:
    print("""Выберите действия:
    1-Добавить книгу
    2-Удалить книгу
    3-Вывести список книг
    4-Поиск
    5-Сортировка по жанрам
    0-Выход""")
    
    responce = input("Ваш выбор: ")
    
    if responce == "0":
        print("Пока!")
        break 
        
    elif responce == "1":
        title = input("Название книги: ")
        author = input("Автор: ")
        genre = input("Жанр: ")
        
        # Добавляем книгу в соответствующий жанр
        if genre not in library:
            library[genre] = []
        library[genre].append(f"{title} - {author}")
        
    elif responce == "2":
        title = input("Название удаляемой книги: ")
        found = False
        for genre in library:
            if title in library[genre]:
                library[genre].remove(title)
                found = True
        if not found:
            print("Книга не найдена!")
            
    elif responce == "3":
        for genre, books in library.items():
            print(f"\nЖанр: {genre}")
            for book in books:
                print(f"- {book}")
                
    elif responce == "4":
        search = input("Поиск книги: ")
        found = False
        for genre, books in library.items():
            for book in books:
                if search in book:
                    print(f"Найденная книга: {book} (Жанр: {genre})")
                    found = True
        if not found:
            print("Книга не найдена!")
            
    elif responce == "5":
        genre = input("Выберите жанр для просмотра: ")
        if genre in library:
            print(f"\nКниги жанра '{genre}':")
            for book in library[genre]:
                print(f"- {book}")
        else:
            print("Жанр не найден!")
            
    else:
        print("Неверный выбор. Попробуйте снова.")
