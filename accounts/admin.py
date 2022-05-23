from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email','is_staff', 'is_active',)
    list_filter = ('email','is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('first_name','middle_name','last_name','mobile_number', 'is_staff', 'is_active','is_superuser','is_admin','is_employee',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','first_name','middle_name','last_name','mobile_number', 'is_staff', 'is_active','is_superuser','is_admin','is_employee',)}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    

admin.site.register(CustomUser, CustomUserAdmin)
