from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm, BookForm


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('create_book', author_id=author.id)
    else:
        form = AuthorForm()
    return render(request, 'create_author.html', {'form': form})


def create_book(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form, 'author': author})
