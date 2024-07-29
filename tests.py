import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_exceeds_length(self, collector):
        collector.add_new_book('B' * 41)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Книга джунглей')
        collector.add_new_book('Книга джунглей')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self, collector):
        collector.add_new_book('Звездные войны')
        collector.set_book_genre('Звездные войны', 'Фантастика')
        assert collector.get_book_genre('Звездные войны') == 'Фантастика'

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('Геркулес')
        collector.set_book_genre('Геркулес', 'InvalidGenre')
        assert collector.get_book_genre('Геркулес') == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Автостопом по галактике')
        collector.add_new_book('Мертвая зона')
        collector.set_book_genre('Автостопом по галактике', 'Фантастика')
        collector.set_book_genre('Мертвая зона', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Автостопом по галактике']

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Мечтают ли андроиды об электроовцах?')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Мечтают ли андроиды об электроовцах?', 'Фантастика')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_for_children() == ['Мечтают ли андроиды об электроовцах?']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('На помощь, Дживс')
        collector.add_book_in_favorites('На помощь, Дживс')
        assert 'На помощь, Дживс' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Илиада')
        collector.add_book_in_favorites('Илиада')
        collector.delete_book_from_favorites('Илиада')
        assert 'Илиада' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Финансист')
        collector.add_new_book('Таинственный остров')
        collector.add_book_in_favorites('Финансист')
        collector.add_book_in_favorites('Таинственный остров')
        assert set(collector.get_list_of_favorites_books()) == {'Финансист', 'Таинственный остров'}

    @pytest.mark.parametrize("book_name, expected", [
        ('B' * 40, True),
        ('B' * 41, False),
        ('', False),
        ('A', True),
    ])
    def test_add_new_book_boundary_values(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected
