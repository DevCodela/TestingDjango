from django.contrib import admin

from .models import Editor, Libro, Autor

admin.site.register(Editor)
admin.site.register(Libro)
admin.site.register(Autor)