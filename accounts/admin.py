from django.contrib import admin
#from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group
# Register your models here.

from .forms import SignUpForm, UserChangeForm



class UserAdmin(BaseUserAdmin):
    """Admin for CustomUserAdmin"""
    #model = User
    form = UserChangeForm
    add_form = SignUpForm
    list_display = ('username', 'email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
       # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'confirm_password')}
        ),
    )
    search_fields = ['username']
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)