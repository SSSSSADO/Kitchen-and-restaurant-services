from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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

class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"


# Dish Views
class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kitchen/dish_form.html"


# Dish-Type Views
class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type"
