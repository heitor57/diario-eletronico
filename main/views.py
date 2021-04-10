from django.shortcuts import render

from django.contrib.auth import login

from django.shortcuts import redirect, render

from django.urls import reverse

from main.forms import CustomUserCreationForm
from .models import Course, Profile

# Create your views here.


def dashboard(request):
    context = {}
    if request.user.id != None:
        courses = []
        # print()
        courses = Course.objects.filter(teacher_id=request.user.id)
        # print(courses)

        context= {'courses':courses}
        print(courses)

    return render(request, "main/dashboard.html",context)

def register(request):

    if request.method == "GET":

        return render(

            request, "main/register.html",

            {"form": CustomUserCreationForm}

        )

    elif request.method == "POST":

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("dashboard"))
