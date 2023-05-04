from django.urls import path
from books.views import book_entry
from books.views import book_view

from books.views import MyModelDeleteView

urlpatterns = [
    path('', book_entry, name='book_entry'),
    path('bookview/',book_view,name='book_view'),
    path('delete/<int:pk>/',MyModelDeleteView.as_view(), name='delete_object'),
]