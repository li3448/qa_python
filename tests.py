import pytest
from pip._internal.index import collector

from main import BooksCollector

class TestBookCollector:
#Проверки на невалидные параметры названия - слишком большое/слишком маленькое
    @pytest.mark.parametrize ('name', ['Как перестать прокрастинировать и начать учить питон', ''])
    def test_add_nonvalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0


#Проверка на добавление жанра книге без названия
    def test_set_book_genre_nameless(self):
     collector = BooksCollector()
     name = '_'
     collector.set_book_genre(name, 'Комедии')
     assert name not in collector.books_genre

#Проверка получения жанра книги по ее имени
    def test_set_book_genre_existing(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если вы хотите убить своего кота')
        collector.set_book_genre('Что делать, если вы хотите убить своего кота', 'Комедии')

        # проверяем,что жанр установлен добавленной книге
        assert collector.get_book_genre('Что делать, если вы хотите убить своего кота') == 'Комедии'

#Проверка добавления несуществующего жанра книге
    def test_set_book_genre__non_existing(self):
        collector = BooksCollector()
        collector.add_new_book('Мечты о море')
        collector.set_book_genre('Мечты о море', 'Драмы')

        # проверяем,что жанр не установлен для книги
        assert collector.get_book_genre('Мечты о море') == 'Драмы'
        assert 'Мечты о море' not in collector.books_genre

#Проверка получения словаря book_genre
    def test_get_books_genre_add_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book("Как получать зарплату 10тыс.р. в минуту")
        collector.set_book_genre("Как получать зарплату 10тыс. в минуту", "Фантастика")

        collector.add_new_book("Как стать миллионером ничего не умея")
        collector.set_book_genre("Как стать миллионером ничего не умея", "Комедии")

        assert collector.get_books_genre() == {"Как получать зарплату 10тыс.р. в минуту":"Фантастика", "Как стать миллионером ничего не умея": "Комедии"}

#Проверка отсутствия взрослой книги в списке детских книг
    def test_no_adult_books_in_children_list(self):
     collector = BooksCollector()
     collector.add_new_book("Кто украл головку сыра")
     collector.set_book_genre("Кто украл головку сыра", "Детективы")
books_for_children = collector.get_books_for_children()
assert "Кто украл головку сыра" not in collector.get_books_for_children



#Проверка добавления книги в избранное
def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Книга о любви")
        collector.add_book_in_favorites("Книга о любви")
        assert collector.get_list_of_favorites_books() == ["Книга о любви"]

#Проверка удаления книги из избранного
def test_delete_book_from_favorites(self):
    collector = BooksCollector()
    collector.add_new_book("Любовь и ненависть")
    collector.add_book_in_favorites("Любовь и ненависть")
    collector.delete_book_from_favorites("Любовь и ненависть")
    assert len(collector.get_list_of_favorites_books()) == 0

 #Проверка получения списка избранных книг
def test_get_list_of_favorites_books(self):
    collector = BooksCollector()
    collector.add_new_book("Любовь и ненависть")
    collector.add_new_book("Книга о любви")
    collector.add_book_in_favorites("Любовь и ненависть")
    collector.add_book_in_favorites("Книга о любви")
    assert collector.get_list_of_favorites_books() == ["Любовь и ненависть", "Книга о любви"]

#Проверка добавления книги отсутствующей в словаре
def test_add_missing_book_in_favorites(self):
    collector = BooksCollector()
    collector.add_new_book("Книга о любви")
    collector.add_book_in_favorites("Книга о котиках")
    assert "Книга о котиках" not in collector.favorites