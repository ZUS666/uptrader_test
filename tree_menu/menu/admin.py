from django.contrib import admin

from menu.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('parent')
