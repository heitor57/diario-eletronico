from django.db import models
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    completed_course = models.BooleanField(default=False)

    # assessments = models.ManyToManyField(Assessment)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='cstudents')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='cteacher')

    def __str__(self):
        return '%s, %s' % (self.id,self.name)
# class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # # role = models.CharField(max_length=50)
    # # is_student = models.BooleanField('student status', default=False)
    # # is_teacher = models.BooleanField('teacher status', default=False)
    # # city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True, verbose_name='Cidade')

    # def __str__(self):
        # return self.user.username

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    subject_taught = models.CharField(max_length=1000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Assessment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (name,type, date, course.name)

class Presence(models.Model):
    present = models.BooleanField()
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    _class = models.ForeignKey(Class,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('student', '_class',)
    # teacher = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='pteacher')

class Evaluation(models.Model):
    rating = models.FloatField()
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('student', 'assessment',)
    # teacher = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='eteacher')

    # evaluations = models.ManyToManyField(Evaluation)

