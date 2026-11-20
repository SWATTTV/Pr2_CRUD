from django.db import models
from django.urls import reverse


class Author(models.Model):
    full_name = models.CharField('ФИО', max_length=180)
    biography = models.TextField('Биография', blank=True)
    photo = models.ImageField('Фотография', upload_to='authors/', blank=True, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('library:author_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField('Название', max_length=120, unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:category_detail', kwargs={'pk': self.pk})


class Publisher(models.Model):
    name = models.CharField('Название', max_length=180)
    city = models.CharField('Город', max_length=100, blank=True)
    website = models.URLField('Сайт', blank=True)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'
        ordering = ['name']

    def __str__(self):
        return self.name


class ReadingRoom(models.Model):
    name = models.CharField('Название зала', max_length=120)
    floor = models.PositiveSmallIntegerField('Этаж', default=1)
    seats = models.PositiveSmallIntegerField('Количество мест', default=20)

    class Meta:
        verbose_name = 'Читальный зал'
        verbose_name_plural = 'Читальные залы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Название книги', max_length=220)
    isbn = models.CharField('ISBN / инвентарный номер', max_length=32, unique=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books', verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='books', verbose_name='Категория')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books', verbose_name='Издательство')
    publication_year = models.PositiveSmallIntegerField('Год издания')
    copies = models.PositiveIntegerField('Количество экземпляров', default=1)
    description = models.TextField('Описание', blank=True)
    cover = models.ImageField('Фото обложки', upload_to='books/', blank=True, null=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.pk})


class Reader(models.Model):
    full_name = models.CharField('ФИО', max_length=180)
    student_card = models.CharField('Номер студенческого билета', max_length=32, unique=True)
    email = models.EmailField('Почта')
    group = models.CharField('Учебная группа', max_length=50)
    photo = models.ImageField('Фотография', upload_to='readers/', blank=True, null=True)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('library:reader_detail', kwargs={'pk': self.pk})


class Librarian(models.Model):
    full_name = models.CharField('ФИО', max_length=180)
    position = models.CharField('Должность', max_length=120, default='Библиотекарь')
    room = models.ForeignKey(ReadingRoom, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Читальный зал')

    class Meta:
        verbose_name = 'Библиотекарь'
        verbose_name_plural = 'Библиотекари'

    def __str__(self):
        return self.full_name


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='loans', verbose_name='Книга')
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT, related_name='loans', verbose_name='Читатель')
    librarian = models.ForeignKey(Librarian, on_delete=models.PROTECT, related_name='loans', verbose_name='Библиотекарь')
    issue_date = models.DateField('Дата выдачи')
    due_date = models.DateField('Вернуть до')
    returned = models.BooleanField('Возвращена', default=False)

    class Meta:
        verbose_name = 'Выдача книги'
        verbose_name_plural = 'Выдачи книг'
        ordering = ['-issue_date', '-pk']

    def __str__(self):
        return f'{self.book} — {self.reader}'

    def get_absolute_url(self):
        return reverse('library:loan_detail', kwargs={'pk': self.pk})
