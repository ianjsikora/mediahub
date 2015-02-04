from django.contrib import admin
from models import Content
from models import Character
from models import Genre
from models import Person


class CharacterAdmin(admin.ModelAdmin):
    fields = ['name','tomato_id']

class ContentAdmin(admin.ModelAdmin):
    fields = ['title','type','release_date','runtime','rating','genre','synopsis','rating_tomato_c','rating_tomato_a','rating_imdb','poster','tomato_id','IMDb_id','cast']

class GenreAdmin(admin.ModelAdmin):
    fields = ['name']

class PersonAdmin(admin.ModelAdmin):
    fields = ['name','type','birthday','headshot','roles']

admin.site.register(Character, CharacterAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Person, PersonAdmin)
