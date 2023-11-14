from django.db.models import Exists, OuterRef

from menu.models import Menu


def get_down_annotated_menu():
    return Exists(
        Menu.objects.filter(parent_id=OuterRef('id'))
    )
