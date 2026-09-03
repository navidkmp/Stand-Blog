from django.contrib import admin
from . import  models

class CommentInline(admin.StackedInline):
    model = models.Comment

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("author","title",)
    list_editable = ("title",)
    search_fields = ("title",)
    inlines = [CommentInline]

admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Footer)