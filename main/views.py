from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login

from django.shortcuts import redirect, render

from django.urls import reverse

# from main.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Class, Assessment
from .forms import AssessmentForm

# Create your views here.


def dashboard(request):
    context = {}
    if request.user.id != None:
        courses = []
        # print()
        courses = Course.objects.filter(teacher_id=request.user.id,
                                        completed_course=False)
        # print(courses)

        context = {'courses': courses}
        print(courses)

    return render(request, "main/dashboard.html", context)


def register(request):

    if request.method == "GET":

        return render(request, "main/register.html", {"form": UserCreationForm})

    elif request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect(reverse("dashboard"))


def course_view(request, course_id):
    context = {'course': Course.objects.filter(id=course_id)[0]}
    # print(context)
    return render(request, "main/course.html", context)


def manage_class_view(request, course_id):
    context = {'course': Course.objects.filter(id=course_id)[0]}

    context['classes'] = Class.objects.filter(course=context['course'].id)
    # print(context['course']._class)

    # print(context)
    return render(request, "main/manage_class.html", context)


def manage_assessment_view(request, course_id):
    context = {'course': Course.objects.filter(id=course_id)[0]}
    context['assessments'] = Assessment.objects.filter(
        course=context['course'].id)
    return render(request, "main/manage_assessment.html", context)


def delete_assessment_view(request, assessment_id):
    # course = Course.objects.filter(id=course_id)[0]
    assessments = Assessment.objects.filter(id=assessment_id)
    if len(assessments) > 0:
        assessment = assessments[0]
        assessment.delete()
        return HttpResponse('<h1>Deletado com sucesso</h1>')
    else:
        return HttpResponse('<h1>Não foi possível deletar</h1>')


def alter_assessment_view(request, assessment_id):
    assessment = Assessment.objects.filter(id=assessment_id)[0]
    if request.method == "GET":
        # course = Course.objects.filter(id=assessment.course)[0]
        form = AssessmentForm(instance=assessment)
        # form.fields['course'].widget.attrs['readonly'] = True
        # form['course'] =
        return render(request, "main/alter_assessment.html", {"form": form})

    elif request.method == "POST":

        form = AssessmentForm(request.POST, instance=assessment)
        # print(form.initial['id'])

        if form.is_valid():
            form.save()

            return HttpResponse('<h1>Salvo</h1>')


def create_assessment_view(request, course_id):
    if request.method == "GET":
        form = AssessmentForm(
            initial={'course': Course.objects.filter(id=course_id)[0]})
        # form.fields['course'].widget.attrs['readonly'] = True
        # form['course'] =
        return render(request, "main/create_assessment.html", {"form": form})

    elif request.method == "POST":

        form = AssessmentForm(request.POST)

        if form.is_valid():

            # print(form)
            user = form.save()
            # login(request, user)

            return HttpResponse('<h1>Salvo</h1>')
