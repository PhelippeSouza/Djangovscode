from django.contrib import admin
from .modelsverao import Post, Category

# Register your models here.
admin.site.register(Post)

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ('nome','criado','publicado')
    list_filter = ('nome','criado','publicado')
    date_hierarchy = 'publicado'
    search_fields = ('nome',)
  