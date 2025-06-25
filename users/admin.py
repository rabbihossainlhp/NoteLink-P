from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ValidRollNumber, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'roll_number', 'depertment', 'is_staff', 'is_active')
    list_filter = ('depertment', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('roll_number','depertment')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('roll_number','depertment')}),
    )

    search_fields = ('email', 'username', 'roll_number', 'depertment')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ValidRollNumber)