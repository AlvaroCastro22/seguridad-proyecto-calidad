from django.urls import path
from .views import UserListCreateView
from .views import (
    MeView,
    MyApplicationsView,
    UsersListView,
    UserDetailView,
    UserApplicationsView,
    GrantAccessView,
    CheckAccessView
)

urlpatterns = [
    # Usuario autenticado
    path('me/', MeView.as_view()),
    path('me/applications/', MyApplicationsView.as_view()),

    # Admin
    path('users/', UsersListView.as_view()),
    path('users/<int:id>/', UserDetailView.as_view()),
    path('users/<int:id>/applications/', UserApplicationsView.as_view()),
    path('access/grant/', GrantAccessView.as_view()),

    # Aplicaciones externas
    path('access/check/', CheckAccessView.as_view()),
    path('users', UserListCreateView.as_view()),
]
