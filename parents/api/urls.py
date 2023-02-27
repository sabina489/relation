from django.urls import path

from parents.api.views import (
    GrandParentsCreateAPIView,
    GrandParentsListAPIView,
    GrandParentsUpdateAPIView,
    GrandParentsDeleteAPIView,
    ParentsCreateAPIView,
    ParentsListAPIView,
    ParentsDeleteAPIView,
    ParentsUpdateAPIView,
    ChildrenCreateAPIView,
    ChildrenListAPIView,
    ChildrenDeleteAPIView,
    ChildrenUpdateAPIView,
    SiblingsCreateAPIView,
    SiblingsListAPIView,
    SiblingsUpdateAPIView,
    SiblingsDeleteAPIView,
)

urlpatterns = [
    path("grandparents/create/", GrandParentsCreateAPIView.as_view()),

    path("grandparents/list/", GrandParentsListAPIView.as_view()),
    path("grandparents/update/<int:pk>", GrandParentsUpdateAPIView.as_view()),
    path("grandparents/delete/<int:pk>", GrandParentsDeleteAPIView.as_view()),

    path("parents/create/", ParentsCreateAPIView.as_view()),
    path("parents/list/", ParentsListAPIView.as_view()),
    path("parents/update/<int:pk>/", ParentsUpdateAPIView.as_view()),
    path("parents/delete/<int:pk>/", ParentsDeleteAPIView.as_view()),

    path("children/create/", ChildrenCreateAPIView.as_view(),name="children-create"),
    path("children/list/", ChildrenListAPIView.as_view()),
    path("children/update/", ChildrenUpdateAPIView.as_view()),
    path("children/delete/", ChildrenDeleteAPIView.as_view()),

    path("siblings/create/", SiblingsCreateAPIView.as_view()),
    path("siblings/list/", SiblingsListAPIView.as_view()),
    path("siblings/update/<int:pk>/", SiblingsUpdateAPIView.as_view()),
    path("siblings/delete/<int:pk>/", SiblingsDeleteAPIView.as_view()),
]
