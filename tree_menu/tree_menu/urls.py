from django.contrib import admin
from django.urls import path

from menu.views import MenuDownView, MenuListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MenuListView.as_view(), name='index'),
    path('<str:name>/', MenuDownView.as_view(), name='detail_menu'),
]
