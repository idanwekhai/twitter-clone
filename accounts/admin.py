from django.contrib import admin
#from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.auth.models import Group
# Register your models here.

from .forms import SignUpForm, UserChangeForm



class UserAdmin(BaseUserAdmin):
    """Admin for CusstomUserAdmin"""
    #model = User
    form = UserChangeForm
    add_form = SignUpForm
    #exclude = ['last_login', 'date_joined']
    list_display = ('username', 'email', 'date_of_birth', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'password', 'confirm_password')}
        ),
    )
    search_fields = ['username']
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)