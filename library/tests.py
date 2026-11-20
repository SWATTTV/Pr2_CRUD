from datetime import date, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import resolve, reverse
from .models import Author, Book, Category, Publisher, Reader, Librarian, Loan, ReadingRoom


class LibraryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(full_name='Тестовый автор')
        cls.category = Category.objects.create(name='Тестовая категория')
        cls.publisher = Publisher.objects.create(name='Тестовое издательство')
        cls.room = ReadingRoom.objects.create(name='Зал №1')
        cls.librarian = Librarian.objects.create(full_name='Тестовый библиотекарь', room=cls.room)
        cls.reader = Reader.objects.create(full_name='Тестовый читатель', student_card='T-001', email='a@example.org', group='ИС-1')
        cls.book = Book.objects.create(title='Тестовая книга', isbn='TEST-001', author=cls.author, category=cls.category, publisher=cls.publisher, publication_year=2026)
        cls.loan = Loan.objects.create(book=cls.book, reader=cls.reader, librarian=cls.librarian, issue_date=date(2026,11,20), due_date=date(2026,12,1))

    def test_eight_models(self):
        from django.apps import apps
        self.assertEqual(len(apps.get_app_config('library').get_models()), 8)

    def test_original_routes(self):
        for name in ['home', 'about', 'contacts', 'location', 'catalog', 'rules']:
            with self.subTest(name=name):
                response = self.client.get(reverse('library:' + name))
                self.assertEqual(response.status_code, 200)

    def test_crud_pages_for_five_models(self):
        for slug, obj in [('book', self.book), ('author', self.author), ('category', self.category), ('reader', self.reader), ('loan', self.loan)]:
            for suffix, kwargs in [('_list', {}), ('_create', {}), ('_detail', {'pk':obj.pk}), ('_update', {'pk':obj.pk}), ('_delete', {'pk':obj.pk})]:
                with self.subTest(slug=slug, suffix=suffix):
                    url = reverse(f'library:{slug}{suffix}', kwargs=kwargs)
                    self.assertEqual(self.client.get(url).status_code, 200)
                    self.assertEqual(resolve(url).url_name, f'{slug}{suffix}')

    def test_book_create_update_delete(self):
        data = {'title': 'Новая книга', 'isbn': 'T-002', 'author': self.author.pk, 'category': self.category.pk, 'publisher': self.publisher.pk, 'publication_year': 2025, 'copies': 3, 'description': 'Описание'}
        r = self.client.post(reverse('library:book_create'), data)
        book = Book.objects.get(isbn='T-002')
        self.assertRedirects(r, book.get_absolute_url())
        data['title'] = 'Изменённая книга'
        self.assertRedirects(self.client.post(reverse('library:book_update', args=[book.pk]), data), book.get_absolute_url())
        self.assertEqual(Book.objects.get(pk=book.pk).title, 'Изменённая книга')
        self.assertRedirects(self.client.post(reverse('library:book_delete', args=[book.pk])), reverse('library:book_list'))
        self.assertFalse(Book.objects.filter(pk=book.pk).exists())

    def test_loan_dates_validation(self):
        bad_data={'book': self.book.pk, 'reader': self.reader.pk, 'librarian': self.librarian.pk, 'issue_date': '2026-11-20', 'due_date': '2026-11-19'}
        response = self.client.post(reverse('library:loan_create'), bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Дата возврата не может быть раньше')

    def test_book_cover_url(self):
        self.book.cover = 'books/book_1.jpg'; self.book.save()
        r = self.client.get(reverse('library:book_detail', args=[self.book.pk]))
        self.assertContains(r, '/media/books/book_1.jpg')
