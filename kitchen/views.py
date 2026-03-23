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


# Cook Views
class CookListView(generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"
    context_object_name = "cook_list"


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"
    context_object_name = "cook"


# Dish Views
class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dish_list"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


# Dish-Type Views
class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
