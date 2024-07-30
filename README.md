Описание тестов

Фикстуры:<br>
Используем фикстуру `collector`, которая создаёт новый экземпляр класса `BooksCollector` для каждого теста, обеспечивая независимость тестов друг от друга.

Тесты:<br>
`test_add_new_book_add_two_books` -
Тест проверяет, что метод `add_new_book` корректно добавляет две книги в коллекцию.

`test_add_new_book_exceeds_length` - Тест проверяет, что книга с длиной названия более 40 символов не добавляется в коллекцию.

`test_add_new_book_duplicate` - 
Тест проверяет, что одну и ту же книгу нельзя добавить в коллекцию дважды.

`test_set_book_genre` - 
Тест проверяет, что метод `set_book_genre` корректно устанавливает жанр для книги.

`test_set_book_genre_invalid` - 
Тест проверяет, что нельзя установить несуществующий жанр для книги.

`test_get_books_with_specific_genre` - 
Тест проверяет, что метод `get_books_with_specific_genre` возвращает правильные книги с указанным жанром.

`test_get_books_for_children` - 
Тест проверяет, что метод `get_books_for_children` возвращает только книги без возрастного рейтинга.

`test_add_book_in_favorites` - 
Тест проверяет, что метод `add_book_in_favorites` корректно добавляет книгу в избранное.

`test_delete_book_from_favorites` - 
Тест проверяет, что метод `delete_book_from_favorites` корректно удаляет книгу из избранного.

`test_get_list_of_favorites_books` - 
Тест проверяет, что метод `get_list_of_favorites_books` возвращает правильный список избранных книг.

`test_add_new_book_boundary_values` - 
Параметризованный тест, который проверяет граничные значения для метода add_new_book. Тестирует следующие случаи:
- Название книги длиной ровно 40 символов.
- Название книги длиной 41 символ.
- Пустое название книги.
- Название книги минимальной длины (1 символ).