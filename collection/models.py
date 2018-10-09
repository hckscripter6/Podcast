from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

class Person(models.Model):
    name = models.CharField(max_length=125)
    bio = RichTextField()

    def __str__(self):
        return "%s" % (self.name)

class Episode(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(storage=S3Boto3Storage(bucket='podcast-app'), null=True, blank=True)
    recording = models.FileField(storage=S3Boto3Storage(bucket='podcast-app'))
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    person = models.ManyToManyField(Person)
    date_added = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % (self.name)

class Update(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % (self.name)



