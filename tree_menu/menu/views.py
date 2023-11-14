from django.http import Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from menu.models import Menu
from menu.services import get_down_annotated_menu


class MenuListView(ListView):
    template_name = 'menu.html'
    queryset = Menu.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(
            parent=None).annotate(
                down=get_down_annotated_menu()
            )

    def get(self, request, *args, **kwargs):
        context = {'menus': self.get_queryset}
        return render(request, self.template_name, context)


class MenuDownView(DetailView):
    template_name = 'menu.html'
    queryset = Menu.objects.all()

    def get_queryset(self, name):
        return super().get_queryset().filter(
            parent__name=name).annotate(
                down=get_down_annotated_menu()
            )

    def get(self, request, name, *args, **kwargs):
        children = self.get_queryset(name)
        if not children:
            raise Http404
        context = {'menus': children}
        return render(request, self.template_name, context)
