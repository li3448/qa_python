from main import BooksCollector
import pytest


class TestBookCollector:

#Проверки на невалидные параметры названия - слишком большое/слишком маленькое
    @pytest.mark.parametrize ('name', ['Как перестать прокрастинировать и начать учить питон', ''])
    def test_add_nonvalid_name(self, name, collector):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0


#Проверка на добавление жанра книге без названия
    def test_set_book_genre_nameless(self, collector):
     name = ''
     collector.add_new_book(name)
     collector.set_book_genre(name, 'Комедии')
     #assert (name, 'Комедии')  not in collector.books_genre
     assert collector.get_book_genre(name) == None

    #проверка на добавление одной книги дважды
    def test_add_new_book_add_one_book_twice(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_genre()) == 1

#Проверка получения жанра книги по ее имени

    def test_add_book_and_set_genre(self, collector):
        collector.add_new_book('Мои жизненные цели')
        collector.set_book_genre('Мои жизненные цели', 'Комедии')
        assert collector.get_book_genre('Мои жизненные цели') == 'Комедии'


#Проверка получения словаря book_genre
    def test_get_books_genre_add_dictionary(self, collector):
        collector.add_new_book("Как получать зарплату 10тыс.р. в минуту")
        collector.set_book_genre("Как получать зарплату 10тыс.р. в минуту", "Фантастика")

        collector.add_new_book("Как стать миллионером ничего не умея")
        collector.set_book_genre("Как стать миллионером ничего не умея", "Комедии")

        assert collector.get_books_genre() == {"Как получать зарплату 10тыс.р. в минуту": "Фантастика", "Как стать миллионером ничего не умея": "Комедии"}


    def test_get_books_for_children(self, collector):
        collector.add_new_book("Улица разбитых фонарей")
        collector.add_new_book("Приключения мумий тролля")
    # Устанавливаем жанры для книг
        collector.set_book_genre("Улица разбитых фонарей", "Детективы")
        collector.set_book_genre("Приключения мумий тролля", "Мультфильмы")

    # Проверяем, что возвращается только книга с жанром "Мультфильмы"
        assert collector.get_books_for_children() == ["Приключения мумий тролля"]

#Проверка добавления книги в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Книга о любви")
        collector.add_book_in_favorites("Книга о любви")
        assert collector.get_list_of_favorites_books() == ["Книга о любви"]

#Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Любовь и ненависть")
        collector.add_book_in_favorites("Любовь и ненависть")
        assert len(collector.get_list_of_favorites_books()) == 1
        collector.delete_book_from_favorites("Любовь и ненависть")
        assert len(collector.get_list_of_favorites_books()) == 0

 #Проверка получения списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Любовь и ненависть")
        collector.add_new_book("Книга о любви")
        collector.add_book_in_favorites("Любовь и ненависть")
        collector.add_book_in_favorites("Книга о любви")
        assert collector.get_list_of_favorites_books() == ["Любовь и ненависть", "Книга о любви"]

#Проверка добавления книги отсутствующей в словаре
    def test_add_missing_book_in_favorites(self, collector):
        collector.add_new_book("Книга о любви")
        collector.add_book_in_favorites("Книга о котиках")
        assert "Книга о котиках" not in collector.favorites