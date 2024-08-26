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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Charmed')
        collector.set_book_genre('Charmed', 'Фантастика')
        assert collector.get_book_genre('Charmed') == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Charmed')
        collector.set_book_genre('Charmed', 'Фантастика')
        collector.add_new_book('The Shining')
        collector.set_book_genre('The Shining', 'Ужасы')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Charmed']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('The Hobbit')
        collector.set_book_genre('The Hobbit', 'Фантастика')
        collector.add_new_book('The Shining')
        collector.set_book_genre('The Shining', 'Ужасы')
        collector.add_new_book('Notes on Sherlock Holmes')
        collector.set_book_genre('Notes on Sherlock Holmes', 'Детективы')
        collector.add_new_book('Frozen')
        collector.set_book_genre('Frozen', 'Мультфильмы')
        expected_books_for_children = ['The Hobbit', 'Frozen']
        assert collector.get_books_for_children() == expected_books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Charmed')
        collector.add_book_in_favorites('Charmed')
        assert 'Charmed' in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book('Charmed')
    collector.set_book_genre('Charmed', 'Фантастика')
    collector.add_book_in_favorites('Charmed')
    favorites = collector.get_list_of_favorites_books()
    assert favorites == ['Charmed']

def test_get_list_of_favorites_books_successfully():
    collector = BooksCollector()
    collector.add_new_book("Charmed")
    collector.set_book_genre("Charmed", "Фантастика")
    collector.add_book_in_favorites("Charmed")
    favorites = collector.get_list_of_favorites_books()
    assert favorites == ["Charmed"]

def test_delete_book_from_favorites_successfully():
    collector = BooksCollector()
    collector.add_new_book("Charmed")
    collector.set_book_genre("Charmed", "Фантастика")
    collector.add_book_in_favorites("Charmed")
    collector.delete_book_from_favorites("Charmed")
    assert "Charmed" not in collector.get_list_of_favorites_books()

@pytest.mark.parametrize("books_and_genres, expected_books_for_children", [
    (
        [("The Hobbit", "Фантастика"), ("The Shining", "Ужасы"), ("Frozen", "Мультфильмы")],
        ["The Hobbit", "Frozen"]
    ),
    (
        [("The Shining", "Ужасы"), ("Notes on Sherlock Holmes", "Детективы")],
        []
    ),
    (
        [("The Hobbit", "Фантастика"), ("Frozen", "Мультфильмы")],
        ["The Hobbit", "Frozen"]
    )
])
def test_get_books_for_children(books_and_genres, expected_books_for_children):
    collector = BooksCollector()
    for book_name, genre in books_and_genres:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

    assert collector.get_books_for_children() == expected_books_for_children

@pytest.mark.parametrize("books_and_genres, expected_books_genre", [
    (
        [("Charmed", "Фантастика"), ("The Shining", "Ужасы")],
        {"Charmed": "Фантастика", "The Shining": "Ужасы"}
    ),
    (
        [("Notes on Sherlock Holmes", "Детективы")],
        {"Notes on Sherlock Holmes": "Детективы"}
    ),
    (
        [],
        {}
    )
])
def test_get_books_genre(books_and_genres, expected_books_genre):
    collector = BooksCollector()
    for book_name, genre in books_and_genres:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

    assert collector.get_books_genre() == expected_books_genre

@pytest.mark.parametrize("book_name, genre, expected_genre", [
    ("Charmed", "Фантастика", "Фантастика"),
    ("The Shining", "", ""),
])
def test_get_book_genre_with_genre(book_name, genre, expected_genre):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected_genre

def test_get_book_genre_for_nonexistent_book():
    collector = BooksCollector()
    assert collector.get_book_genre("None Book") is None