from django.contrib import admin
# from .models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# class ProfileInline(admin.StackedInline):
    # model = Profile
    # can_delete = False
    # fk_name = 'user'
# class CustomUserAdmin(UserAdmin):

    # inlines = (ProfileInline, )

    # def get_inline_instances(self, request, obj=None):
        # if not obj:
            # return list()
        # return super(CustomUserAdmin, self).get_inline_instances(request, obj)


# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
# Register your models here.
