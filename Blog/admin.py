from django.contrib import admin

from .models import Post,Category

@admin.register(Post)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'auth', 'slug', 'created','active']
    list_filter = ['created','active']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_filter = ['title',]
    search_fields = ['title', ]
    prepopulated_fields = {'slug': ('title',)}

