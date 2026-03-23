from django.urls import path
from kitchen import views


app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    # Cook paths
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    # Dish paths
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    # Dish-Type paths
    path(
        "dish-types/",
        views.DishTypeListView.as_view(),
        name="dish-type-list"
    ),
]