from django.contrib import admin
from .models import Category, Location, Post

# Настройка админ-панели для модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'description')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'description', 'is_published')
        }),
        ('Дата создания', {
            'fields': ('created_at',)
        }),
    )

# Настройка админ-панели для модели Location
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'is_published')
        }),
        ('Дата создания', {
            'fields': ('created_at',)
        }),
    )

# Настройка админ-панели для модели Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published', 'created_at')
    list_filter = ('is_published', 'author', 'category', 'location')
    search_fields = ('title', 'text')

    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'author', 'category', 'location', 'is_published')
        }),
        ('Дата публикации', {
            'fields': ('pub_date', 'created_at')
        }),
    )

# Регистрация моделей в админ-панели
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)

# Перевод названий на русский язык
admin.site.site_header = "Блог"
admin.site.site_title = "Администрирование блога"
admin.site.index_title = "Управление блогом"