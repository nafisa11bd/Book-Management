from django.shortcuts import redirect,render
from .forms import Bookentry
from books.models import Book
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


def book_entry(request):
    context ={}
    form = Bookentry(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "bookentry.html", context)

# Create your views here.
def book_view(request):
    data=Book.objects.all()
    return render(request, 'bookview.html', {'data': data})

class MyModelDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('bookview')
    