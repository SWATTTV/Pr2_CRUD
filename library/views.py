from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AuthorForm, CategoryForm, BookForm, ReaderForm, LoanForm
from .models import Author, Category, Book, Reader, Loan


def home(request):
    return render(request, 'library/home.html')


def about(request):
    return render(request, 'library/about.html')


def contacts(request):
    return render(request, 'library/contacts.html')


def location(request):
    return render(request, 'library/location.html')


def rules(request):
    return render(request, 'library/rules.html')


class EntityViewMixin:
    template_name = 'library/entity_list.html'
    entity_title = ''
    entity_slug = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_title'] = self.entity_title
        context['entity_slug'] = self.entity_slug
        return context


class EntityDetailMixin(EntityViewMixin):
    template_name = 'library/entity_detail.html'


class EntityFormMixin(EntityViewMixin):
    template_name = 'library/entity_form.html'


class EntityDeleteMixin(EntityViewMixin):
    template_name = 'library/entity_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(f'library:{self.entity_slug}_list')


class BookList(EntityViewMixin, ListView):
    model = Book
    entity_slug = 'book'
    entity_title = 'Книги'
    queryset = Book.objects.select_related('author', 'category', 'publisher')


class BookDetail(EntityDetailMixin, DetailView):
    model = Book
    entity_slug = 'book'
    entity_title = 'Книга'


class BookCreate(EntityFormMixin, CreateView):
    model = Book
    form_class = BookForm
    entity_slug = 'book'
    entity_title = 'Добавление книги'


class BookUpdate(EntityFormMixin, UpdateView):
    model = Book
    form_class = BookForm
    entity_slug = 'book'
    entity_title = 'Редактирование книги'


class BookDelete(EntityDeleteMixin, DeleteView):
    model = Book
    entity_slug = 'book'
    entity_title = 'Удаление книги'


class AuthorList(EntityViewMixin, ListView):
    model = Author
    entity_slug = 'author'
    entity_title = 'Авторы'


class AuthorDetail(EntityDetailMixin, DetailView):
    model = Author
    entity_slug = 'author'
    entity_title = 'Автор'


class AuthorCreate(EntityFormMixin, CreateView):
    model = Author
    form_class = AuthorForm
    entity_slug = 'author'
    entity_title = 'Добавление автора'


class AuthorUpdate(EntityFormMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    entity_slug = 'author'
    entity_title = 'Редактирование автора'


class AuthorDelete(EntityDeleteMixin, DeleteView):
    model = Author
    entity_slug = 'author'
    entity_title = 'Удаление автора'


class CategoryList(EntityViewMixin, ListView):
    model = Category
    entity_slug = 'category'
    entity_title = 'Категории'


class CategoryDetail(EntityDetailMixin, DetailView):
    model = Category
    entity_slug = 'category'
    entity_title = 'Категория'


class CategoryCreate(EntityFormMixin, CreateView):
    model = Category
    form_class = CategoryForm
    entity_slug = 'category'
    entity_title = 'Добавление категории'


class CategoryUpdate(EntityFormMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    entity_slug = 'category'
    entity_title = 'Редактирование категории'


class CategoryDelete(EntityDeleteMixin, DeleteView):
    model = Category
    entity_slug = 'category'
    entity_title = 'Удаление категории'


class ReaderList(EntityViewMixin, ListView):
    model = Reader
    entity_slug = 'reader'
    entity_title = 'Читатели'


class ReaderDetail(EntityDetailMixin, DetailView):
    model = Reader
    entity_slug = 'reader'
    entity_title = 'Читатель'


class ReaderCreate(EntityFormMixin, CreateView):
    model = Reader
    form_class = ReaderForm
    entity_slug = 'reader'
    entity_title = 'Добавление читателя'


class ReaderUpdate(EntityFormMixin, UpdateView):
    model = Reader
    form_class = ReaderForm
    entity_slug = 'reader'
    entity_title = 'Редактирование читателя'


class ReaderDelete(EntityDeleteMixin, DeleteView):
    model = Reader
    entity_slug = 'reader'
    entity_title = 'Удаление читателя'


class LoanList(EntityViewMixin, ListView):
    model = Loan
    entity_slug = 'loan'
    entity_title = 'Выдачи книг'
    queryset = Loan.objects.select_related('book', 'reader', 'librarian')


class LoanDetail(EntityDetailMixin, DetailView):
    model = Loan
    entity_slug = 'loan'
    entity_title = 'Выдача книги'


class LoanCreate(EntityFormMixin, CreateView):
    model = Loan
    form_class = LoanForm
    entity_slug = 'loan'
    entity_title = 'Регистрация выдачи'


class LoanUpdate(EntityFormMixin, UpdateView):
    model = Loan
    form_class = LoanForm
    entity_slug = 'loan'
    entity_title = 'Редактирование выдачи'


class LoanDelete(EntityDeleteMixin, DeleteView):
    model = Loan
    entity_slug = 'loan'
    entity_title = 'Удаление выдачи'
