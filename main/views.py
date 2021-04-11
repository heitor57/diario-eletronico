from django.shortcuts import render
from django.http import HttpResponse
import django.forms.fields

from django.contrib.auth import login

from django.shortcuts import redirect, render

from django.urls import reverse

# from main.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Course, Class, Assessment
from .forms import AssessmentForm
import django.forms.models

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
    assessment = Assessment.objects.filter(id=assessment_id)[0]
    if assessment:
        # assessment = assessments[0]
        assessment.delete()
        return render(request, "main/simple_message.html",{'message': 'Deletado com sucesso','url_back':reverse('manage_assessment',kwargs={'course_id':assessment.course_id})})
    else:
        return render(request, "main/simple_message.html",{'message': 'Não foi possível deletar','url_back':reverse('manage_assessment',kwargs={'course_id':assessment.course_id})})


def alter_assessment_view(request, assessment_id):
    assessment = Assessment.objects.filter(id=assessment_id)[0]
    if request.method == "GET":
        # course = Course.objects.filter(id=assessment.course)[0]
        form = AssessmentForm(instance=assessment)
        form.fields['course'].queryset= Course.objects.filter(teacher=request.user.id,
                                           completed_course=False)
        # form.fields['course'].widget.attrs['readonly'] = True
        # form['course'] =
        return render(request, "main/alter_assessment.html", {"form": form})

    elif request.method == "POST":

        form = AssessmentForm(request.POST, instance=assessment)
        # print(form.initial['id'])

        if form.is_valid():
            user = form.save()
            return render(request, "main/simple_message.html",{'message': 'Salvo com sucesso','url_back':reverse('manage_assessment',kwargs={'course_id':assessment.course_id})})
        else:
            form.fields['course'].queryset= Course.objects.filter(teacher=request.user.id,
                                               completed_course=False)
            return render(request, "main/create_assessment.html",
                          {"form": form})


def create_assessment_view(request, course_id):
    course = Course.objects.filter(id=course_id)[0]
    if request.method == "GET":
        form = AssessmentForm(initial={'course': course})
        # form.fields['course'] = django.forms.models.ModelChoiceField(
            # queryset=Course.objects.filter(teacher=request.user.id,
                                           # completed_course=False))
        form.fields['course'].queryset= Course.objects.filter(teacher=request.user.id,
                                           completed_course=False)
        # form.
        return render(request, "main/create_assessment.html", {"form": form})

    elif request.method == "POST":
        form = AssessmentForm(request.POST, initial={'course': course})
        if form.is_valid():
            user = form.save()
                # return HttpResponse('<h1>Salvo</h1>')
            return render(request, "main/simple_message.html",{'message': 'Salvo com sucesso','url_back':reverse('manage_assessment',kwargs={'course_id':course.id})})
        else:
            form.fields['course'].queryset= Course.objects.filter(teacher=request.user.id,
                                               completed_course=False)
            return render(request, "main/create_assessment.html",
                          {"form": form})
