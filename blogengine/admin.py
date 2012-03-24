import models
from django.contrib import admin
from django.contrib.auth.models import User

class CategoryInline(admin.TabularInline):
    model = models.Post.categories.through
    extra = 0

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryInline]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(models.Post, PostAdmin)
