from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from kitchen.models import Cook, DishType, Dish


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "num_cook": Cook.objects.all().count(),
        "num_dish_type": DishType.objects.all().count(),
        "num_dish": Dish.objects.all().count(),
    }
    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cook_list"
