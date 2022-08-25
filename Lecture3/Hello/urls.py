from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),# frist one
    path("brian", views.brian, name="brian"),# user-defined
    path("david", views.david, name="david"),# user-defined
    path("<str:name>", views.greet, name="greet")# templates for name
]