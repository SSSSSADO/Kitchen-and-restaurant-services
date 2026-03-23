from django.urls import path
from kitchen import views


app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    # Cook paths
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/",
        views.CookDetailView.as_view(),
        name="cook-detail"
    ),
    # Dish paths
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path(
        "dishes/<int:pk>/",
        views.DishDetailView.as_view(),
        name="dish-detail"
    ),
    # Dish-Type paths
    path(
        "dish-types/",
        views.DishTypeListView.as_view(),
        name="dish-type-list"
    ),
]