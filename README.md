# Библиотека ВУЗа — практическая работа: модели, миграции, CRUD и медиа

Продолжение предыдущей работы по маршрутизации. Реализованы **8 таблиц Django**, **5 полных CRUD** на основе generic views, HTML-шаблоны с Django template tags, загрузка изображений и единый стиль.

## Запуск в Windows (VS Code)

Откройте терминал в распакованной папке, где лежит `manage.py`.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_library
python manage.py runserver
```

Если PowerShell запрещает активацию, запускайте команды через `.venv\Scripts\python.exe`. Откройте **http://127.0.0.1:8000/**.

> `seed_library` заполняет все 8 таблиц примерами, создаёт книги, читателей и выдачу. Демонстрационные картинки уже лежат в папке `media`. Команда повторно не создаёт одинаковые записи. Данные вымышленные и предназначены исключительно для учебного проекта.

## Таблицы (в `library/models.py`)

1. `Author` — автор (фотография).
2. `Category` — категория литературы.
3. `Publisher` — издательство.
4. `ReadingRoom` — читальный зал.
5. `Book` — книга (обложка, связи с автором, категорией и издательством).
6. `Reader` — читатель (фотография).
7. `Librarian` — библиотекарь (связь с читальным залом).
8. `Loan` — выдача книги (связи с книгой, читателем, библиотекарем).

## CRUD для 5 таблиц

| Модель | Список | Детали | Добавить | Изменить | Удалить |
|---|---|---|---|---|---|
| Книга | `/books/` | `/books/1/` | `/books/add/` | `/books/1/edit/` | `/books/1/delete/` |
| Автор | `/authors/` | `/authors/1/` | `/authors/add/` | `/authors/1/edit/` | `/authors/1/delete/` |
| Категория | `/categories/` | `/categories/1/` | `/categories/add/` | `/categories/1/edit/` | `/categories/1/delete/` |
| Читатель | `/readers/` | `/readers/1/` | `/readers/add/` | `/readers/1/edit/` | `/readers/1/delete/` |
| Выдача | `/loans/` | `/loans/1/` | `/loans/add/` | `/loans/1/edit/` | `/loans/1/delete/` |

Все ссылки генерируются по **имени URL**, а URL определены только в `library/urls.py` (в `university_library/urls.py` только `include`, `/admin/` и раздача media при `DEBUG=True`).

Для каждой операции есть соответствующий URL и отдельная страница, а для однотипных действий общие HTML-шаблоны `entity_list.html`, `entity_detail.html`, `entity_form.html`, `entity_confirm_delete.html`. Они используют теги Django (`for`, `if`, `url`, `csrf_token`) и переменные (`{{ object }}`). Страницы `home`, `about`, `contacts`, `location`, `rules` остались из предыдущей работы.

Фотографии/обложки загружаются в `media/authors/`, `media/readers/`, `media/books/`, а в шаблонах используются `{{ object.photo.url }}` / `{{ object.cover.url }}`. Изображения из примеров являются условными иллюстрациями; реальные фотографии можно загрузить через формы.

В рамках учебного проекта CRUD доступен без авторизации. Для размещения в интернете нужно ограничить операции пользователями с соответствующими правами, выключить `DEBUG`, настроить хранилище media и секретный ключ.

## Проверка

```powershell
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Дополнительная таблица

Создайте администратора `python manage.py createsuperuser` и откройте `/admin/` — через панель администратора доступны все 8 моделей, включая издательства, читальные залы и библиотекарей.

## Что сфотографировать для отчёта

- Команды `migrate`, `seed_library`, `runserver` в терминале.
- Структуру 8 моделей в `models.py` и созданную миграцию.
- Общий список книг и страницу с фотографией обложки.
- Формы создания, редактирования и удаления одной из книг.
- Список авторов с фотографиями и список читателей.
- Список выдач и подробности выдачи.
- `library/urls.py` и `university_library/urls.py` для подтверждения раздельной маршрутизации.

## Git

Создайте пустой репозиторий на GitHub, затем из папки проекта выполните:

```bash
git init
git add .
git commit -m "Практическая работа: Django CRUD библиотеки ВУЗа"
git branch -M main
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

Настоящая ссылка на GitHub появится после вашей публикации.
