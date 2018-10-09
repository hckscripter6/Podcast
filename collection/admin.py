from django.contrib import admin
from collection.models import Episode, Tag, Category

# Register your models here.
admin.site.register(Episode)
admin.site.register(Category)
admin.site.register(Tag)
