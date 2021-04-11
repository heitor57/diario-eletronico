from django.urls import path,include

from django.views.generic import TemplateView

from django.conf.urls import url
# from main.views import dashboard

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # url(r"^dashboard/", views.dashboard, name="dashboard"),
    # url(r"^", views.dashboard, name="dashboard"),
    url(r'^courses/(?P<course_id>\w+)', views.course_view, name='course_view'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^register/", views.register, name="register"),
    url(r"^manage_class/(?P<course_id>\w+)",views.manage_class_view,name='manage_class'),
    url(r"^manage_assessment/(?P<course_id>\w+)",views.manage_assessment_view,name='manage_assessment'),

    url(r"^create_assessment/(?P<course_id>\w+)",views.create_assessment_view,name='create_assessment'),
    url(r"^delete_assessment/(?P<assessment_id>\d+)",views.delete_assessment_view,name='delete_assessment'),
    url(r"^alter_assessment/(?P<assessment_id>\d+)",views.alter_assessment_view,name='alter_assessment'),
    # url(r"^register/", TemplateView.as_view(template_name='foo.html')),

]
