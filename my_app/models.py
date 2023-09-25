from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, help_text="ФИО Автора")

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, help_text="Название Книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f"{self.title} - {self.author.name}"
