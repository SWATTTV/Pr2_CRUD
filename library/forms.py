from django import forms
from .models import Author, Category, Book, Reader, Loan


class DateInput(forms.DateInput):
    input_type = 'date'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['full_name', 'biography', 'photo']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'author', 'category', 'publisher', 'publication_year', 'copies', 'description', 'cover']


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['full_name', 'student_card', 'email', 'group', 'photo']


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['book', 'reader', 'librarian', 'issue_date', 'due_date', 'returned']
        widgets = {'issue_date': DateInput(), 'due_date': DateInput()}

    def clean(self):
        data = super().clean()
        issued, due = data.get('issue_date'), data.get('due_date')
        if issued and due and due < issued:
            self.add_error('due_date', 'Дата возврата не может быть раньше даты выдачи.')
        return data
