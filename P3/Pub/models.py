from django.db import models


# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/category/', null=True)

    def __str__(self):
        return f"ID: {self.category_id}, {self.category_name}"


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}/{self.country.name}"


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=10, unique=True)
    store_address = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, related_name='stores', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='stores', on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.store_name


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, related_name='authors', on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='authors', on_delete=models.CASCADE)
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=20, unique=True)
    category = models.ManyToManyField(Category, related_name='publishers', blank=True)
    date_established = models.DateField()

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=20, unique=True)
    category = models.ManyToManyField(Category, related_name='books')
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    date_published = models.DateField()
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.book_name}/{self.price}R"
