from django.db import models

# Create your models here.
class Book(models.Model):
	
	Language = models.TextField(unique=False)
	DDC = models.TextField(unique=False)
	Title = models.TextField(unique=False)
	Author = models.TextField(unique=False)
	Titleorg = models.TextField(unique=False)
	Vol = models.TextField(unique=False)
	Edition = models.TextField(unique=False)
	Series = models.TextField(unique=False)
	Year = models.TextField(unique=False)
	publisher = models.TextField(unique=False)
	Preface = models.TextField(unique=False)
	Illustrator = models.TextField(unique=False)
	Pages = models.TextField(unique=False)
	Length = models.TextField(unique=False)
	Price = models.TextField(unique=False)
	Note = models.TextField(unique=False)
	Location = models.TextField(unique=False)

class DDC(models.Model):
	
	DDC = models.TextField(unique=False)
	subject= models.TextField(unique=False)

class Author(models.Model):

	Author = models.TextField(unique=False)

class Title_word(models.Model):

	word = models.TextField(unique=False)
	
