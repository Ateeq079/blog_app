from django.contrib import admin
from .models import Article, Category, ImageModel, Comment
from django.utils.html import format_html

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image and obj.image.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(ImageModel)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'date_posted')
    search_fields = ('post__title', "author__username")