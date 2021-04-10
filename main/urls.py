from django.urls import path,include

from django.conf.urls import url
# from main.views import dashboard

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # url(r"^dashboard/", views.dashboard, name="dashboard"),
    # url(r"^", views.dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^register/", views.register, name="register"),
]
