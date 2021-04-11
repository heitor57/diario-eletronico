from django.db import models
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    id = models.CharField(max_length=50,primary_key=True,verbose_name='Identificador')
    name = models.CharField(max_length=50,verbose_name='Nome')
    completed_course = models.BooleanField(default=False,verbose_name='Finalizado?')

    # assessments = models.ManyToManyField(Assessment)
    students = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='cstudents',verbose_name='Estudantes')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='cteacher',verbose_name='Professor')

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
    date = models.DateTimeField(auto_now_add=True,verbose_name='Data')
    subject_taught = models.CharField(max_length=1000,verbose_name='Matéria lecionada')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Disciplina')

class Assessment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name='Nome')
    type = models.CharField(max_length=50,verbose_name='Tipo')
    date = models.DateTimeField(verbose_name='Data')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name='Disciplina')

    def __str__(self):
        return '%s %s %s %s' % (name,type, date, course.name)

class Presence(models.Model):
    present = models.BooleanField(verbose_name='Presente?')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='Estudante')
    _class = models.ForeignKey(Class,on_delete=models.CASCADE,verbose_name='Aula')
    class Meta:
        unique_together = ('student', '_class',)
    # teacher = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='pteacher')

class Evaluation(models.Model):
    rating = models.FloatField(verbose_name='Nota')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='Estudante')
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,verbose_name='Avaliação')
    class Meta:
        unique_together = ('student', 'assessment',)
    # teacher = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='eteacher')

    # evaluations = models.ManyToManyField(Evaluation)

