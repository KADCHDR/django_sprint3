from django.contrib import admin
from .models import Category, Location, Post
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {'fields': ('title', 'description', 'slug')}),
        ('Дополнительно', {'fields': ('is_published', 'created_at')}),
    )

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    readonly_fields = ('created_at',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date', 'is_published', 'category', 'location')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'pub_date', 'category')
    search_fields = ('title', 'text')
    readonly_fields = ('created_at',)