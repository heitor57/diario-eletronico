from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(UserCreationForm):
# class Meta(UserCreationForm.Meta):
# fields = UserCreationForm.Meta.fields + ("email")


class CustomUserCreationForm(UserCreationForm):
    # job_title = forms.CharField(max_length=100, required=True)
    is_teacher = forms.BooleanField(required=False)
    is_student = forms.BooleanField(required=False)

    # class Meta:
        # model = User
        # fields = ('password')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_profile = Profile(user=user,
                               is_student=self.cleaned_data['is_student'],
                               is_teacher=self.cleaned_data['is_teacher'])
        user_profile.save()
        return user, user_profile
