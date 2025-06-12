from django.contrib import admin
from .models import Post

# Register your models here.

# Aby nasz model był widoczny w panelu admina, musimy go zarejestrować za pomocą poniższego polecenia
admin.site.register(Post)

