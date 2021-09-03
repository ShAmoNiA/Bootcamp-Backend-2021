from django.db import models
from django.db.models.base import Model


class Author(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    name = models.CharField(max_length=250, default='unknown')
    gender = models.CharField(max_length=10, default=MALE)
    dead = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.name} : {self.gender}'

    class Meta:
        db_table = 'Author'


class Book(models.Model):
    name = models.CharField(max_length=250, blank=True)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    published = models.DateField(verbose_name='Publishe_date', blank=True)

    class Meta:
        db_table = 'books'
