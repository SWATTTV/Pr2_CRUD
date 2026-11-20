from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('location/', views.location, name='location'),
    path('catalog/', views.BookList.as_view(), name='catalog'),
    path('rules/', views.rules, name='rules'),
]

for prefix, list_view, detail_view, create_view, update_view, delete_view in [
    ('book', views.BookList, views.BookDetail, views.BookCreate, views.BookUpdate, views.BookDelete),
    ('author', views.AuthorList, views.AuthorDetail, views.AuthorCreate, views.AuthorUpdate, views.AuthorDelete),
    ('category', views.CategoryList, views.CategoryDetail, views.CategoryCreate, views.CategoryUpdate, views.CategoryDelete),
    ('reader', views.ReaderList, views.ReaderDetail, views.ReaderCreate, views.ReaderUpdate, views.ReaderDelete),
    ('loan', views.LoanList, views.LoanDetail, views.LoanCreate, views.LoanUpdate, views.LoanDelete),
]:
    urlpatterns += [
        path(f'{prefix}s/' if prefix != 'category' else 'categories/', list_view.as_view(), name=f'{prefix}_list'),
        path(f'{prefix}s/add/' if prefix != 'category' else 'categories/add/', create_view.as_view(), name=f'{prefix}_create'),
        path(f'{prefix}s/<int:pk>/' if prefix != 'category' else 'categories/<int:pk>/', detail_view.as_view(), name=f'{prefix}_detail'),
        path(f'{prefix}s/<int:pk>/edit/' if prefix != 'category' else 'categories/<int:pk>/edit/', update_view.as_view(), name=f'{prefix}_update'),
        path(f'{prefix}s/<int:pk>/delete/' if prefix != 'category' else 'categories/<int:pk>/delete/', delete_view.as_view(), name=f'{prefix}_delete'),
    ]
