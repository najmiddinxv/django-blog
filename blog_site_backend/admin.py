from django.contrib import admin

from .models import Tag, Categories

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # list_display = ['image', 'get_versions']
    # def get_versions(self, obj):
    #     return obj.versions

    # get_versions.short_description = 'Versions'
    # readonly_fields = ('get_versions',)
    pass

