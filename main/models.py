from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # role = models.CharField(max_length=50)
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    # city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True, verbose_name='Cidade')

    def __str__(self):
        return self.user.username

class Presence(models.Model):
    present = models.BooleanField()
    student = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='pstudent')
    teacher = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='pteacher')

class Evaluation(models.Model):
    rating = models.FloatField()
    student = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='estudent')
    teacher = models.OneToOneField(Profile, on_delete=models.CASCADE,related_name='eteacher')

class Class(models.Model):
    date = models.DateTimeField()
    subject_taught = models.CharField(max_length=1000)
    presences = models.ManyToManyField(Presence)

class Assessment(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    date = models.DateTimeField()
    classes = models.ManyToManyField(Class)

class Course(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    completed_course = models.BooleanField(default=False)

    assessments = models.ManyToManyField(Assessment)
    students = models.ManyToManyField(Profile,related_name='cstudents')
    teacher = models.OneToOneField(Profile,on_delete=models.SET_NULL,null=True,related_name='cteacher')


# c = Book.create(id='MAT')
# c.save()

# class User(AbstractUser):
    # is_student = models.BooleanField('student status', default=False)
    # is_teacher = models.BooleanField('teacher status', default=False)
