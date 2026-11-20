from datetime import date, timedelta
from django.core.management.base import BaseCommand
from library.models import Author, Category, Publisher, ReadingRoom, Book, Reader, Librarian, Loan


class Command(BaseCommand):
    help = 'Создать демонстрационные записи для восьми таблиц (запускать после migrate)'

    def handle(self, *args, **kwargs):
        authors = [
            Author.objects.get_or_create(full_name='Александр Иванов', defaults={'biography': 'Автор учебных материалов по программированию.', 'photo': 'authors/author_1.jpg'})[0],
            Author.objects.get_or_create(full_name='Мария Смирнова', defaults={'biography': 'Специалист по базам данных и информационным системам.', 'photo': 'authors/author_2.jpg'})[0],
        ]
        categories = [
            Category.objects.get_or_create(name='Программирование', defaults={'description': 'Учебники по языкам программирования.'})[0],
            Category.objects.get_or_create(name='Базы данных', defaults={'description': 'Проектирование и работа с СУБД.'})[0],
        ]
        publisher = Publisher.objects.get_or_create(name='Университетское издательство', defaults={'city': 'Москва'})[0]
        room = ReadingRoom.objects.get_or_create(name='Главный читальный зал', defaults={'floor': 2, 'seats': 48})[0]
        librarian = Librarian.objects.get_or_create(full_name='Елена Петрова', defaults={'room': room})[0]
        book_specs = [
            ('Основы Python', 'DEMO-001', authors[0], categories[0], 'books/book_1.jpg', 2024),
            ('Проектирование баз данных', 'DEMO-002', authors[1], categories[1], 'books/book_2.jpg', 2025),
            ('Практикум по Django', 'DEMO-003', authors[0], categories[0], 'books/book_3.jpg', 2026),
        ]
        books = []
        for title, isbn, author, category, cover, year in book_specs:
            book, _ = Book.objects.get_or_create(isbn=isbn, defaults={'title': title, 'author': author, 'category': category, 'publisher': publisher, 'publication_year': year, 'copies': 5, 'description': 'Учебное издание для студентов университета.', 'cover': cover})
            books.append(book)
        reader = Reader.objects.get_or_create(student_card='ST-001', defaults={'full_name': 'Иван Соколов', 'email': 'student@example.org', 'group': 'ИС-50', 'photo': 'readers/reader_1.jpg'})[0]
        Loan.objects.get_or_create(book=books[0], reader=reader, librarian=librarian, issue_date=date(2026, 11, 20), defaults={'due_date': date(2026, 12, 4)})
        self.stdout.write(self.style.SUCCESS('Демонстрационные записи добавлены.'))
