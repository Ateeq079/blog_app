from django.contrib import admin
from .models import Article, Category, ImageModel , Comment
# Register your models here.
@admin.register(Article)
@admin.register(ImageModel)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'date_posted')
    search_fields = ('post__title', "author__username")