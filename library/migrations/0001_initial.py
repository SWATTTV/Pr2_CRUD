from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('full_name', models.CharField(max_length=180, verbose_name='ФИО')), ('biography', models.TextField(blank=True, verbose_name='Биография')), ('photo', models.ImageField(blank=True, null=True, upload_to='authors/', verbose_name='Фотография'))],
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы', 'ordering': ['full_name']},
        ),
        migrations.CreateModel(
            name='Category',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('name', models.CharField(max_length=120, unique=True, verbose_name='Название')), ('description', models.TextField(blank=True, verbose_name='Описание'))],
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('name', models.CharField(max_length=180, verbose_name='Название')), ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')), ('website', models.URLField(blank=True, verbose_name='Сайт'))],
            options={'verbose_name': 'Издательство', 'verbose_name_plural': 'Издательства', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='ReadingRoom',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('name', models.CharField(max_length=120, verbose_name='Название зала')), ('floor', models.PositiveSmallIntegerField(default=1, verbose_name='Этаж')), ('seats', models.PositiveSmallIntegerField(default=20, verbose_name='Количество мест'))],
            options={'verbose_name': 'Читальный зал', 'verbose_name_plural': 'Читальные залы', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Book',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('title', models.CharField(max_length=220, verbose_name='Название книги')), ('isbn', models.CharField(max_length=32, unique=True, verbose_name='ISBN / инвентарный номер')), ('publication_year', models.PositiveSmallIntegerField(verbose_name='Год издания')), ('copies', models.PositiveIntegerField(default=1, verbose_name='Количество экземпляров')), ('description', models.TextField(blank=True, verbose_name='Описание')), ('cover', models.ImageField(blank=True, null=True, upload_to='books/', verbose_name='Фото обложки')), ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.author', verbose_name='Автор')), ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.category', verbose_name='Категория')), ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.publisher', verbose_name='Издательство'))],
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги', 'ordering': ['title']},
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('full_name', models.CharField(max_length=180, verbose_name='ФИО')), ('student_card', models.CharField(max_length=32, unique=True, verbose_name='Номер студенческого билета')), ('email', models.EmailField(max_length=254, verbose_name='Почта')), ('group', models.CharField(max_length=50, verbose_name='Учебная группа')), ('photo', models.ImageField(blank=True, null=True, upload_to='readers/', verbose_name='Фотография'))],
            options={'verbose_name': 'Читатель', 'verbose_name_plural': 'Читатели', 'ordering': ['full_name']},
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('full_name', models.CharField(max_length=180, verbose_name='ФИО')), ('position', models.CharField(default='Библиотекарь', max_length=120, verbose_name='Должность')), ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.readingroom', verbose_name='Читальный зал'))],
            options={'verbose_name': 'Библиотекарь', 'verbose_name_plural': 'Библиотекари'},
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('issue_date', models.DateField(verbose_name='Дата выдачи')), ('due_date', models.DateField(verbose_name='Вернуть до')), ('returned', models.BooleanField(default=False, verbose_name='Возвращена')), ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='library.book', verbose_name='Книга')), ('reader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='library.reader', verbose_name='Читатель')), ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loans', to='library.librarian', verbose_name='Библиотекарь'))],
            options={'verbose_name': 'Выдача книги', 'verbose_name_plural': 'Выдачи книг', 'ordering': ['-issue_date', '-pk']},
        ),
    ]
