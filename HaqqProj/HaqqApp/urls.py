from django.urls import path
from .views import (
    EmployerSignupView,
    RefugeeSignupView,
    HomeView
)

urlpatterns = [
    path('employer_signup/', EmployerSignupView.as_view(), name='employer_signup'),
    path('refugee_signup/', RefugeeSignupView.as_view(), name='refugee_signup'),
    path('', HomeView.as_view(), name='home'),
]