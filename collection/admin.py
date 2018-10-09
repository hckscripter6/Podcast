from django.contrib import admin
from collection.models import Episode, Tag, Category, Person

# Register your models here.
admin.site.register(Episode)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Person)
