from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'gender', 'is_active', 'last_login',)
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_manager', 'is_superuser', 'is_active')
    fieldsets = (
        ('User Credential', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', ('profilePicture',),)}),
        ('Permissions', {'fields': (('is_active', 'is_staff', 'is_manager', 'is_superuser'), 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        ('New User', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'gender',),
        }),
        ('User Credential', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
        ('Permission', {
            'classes': ('collapse',),
            'fields': (('is_active', 'is_staff', 'is_manager', 'is_superuser'), 'user_permissions',),
        }),
    )
    ordering = ('email',)
    list_editable = ()
    list_per_page = 10
    date_hierarchy = ('date_joined')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.unregister(Group)
