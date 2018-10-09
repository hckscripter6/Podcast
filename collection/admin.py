from django.contrib import admin
from collection.models import Episode, Tag, Category, Person

class EpisodeAdmin(admin.ModelAdmin):
    model = Episode
    list_display = ('name',)
    prepopulated_fields={'slug':('name',)}

# Register your models here.
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Person)
