from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "name", "is_admin", "tc", "created_at"]
    list_filter = ["is_admin"]

    # Responsible to display fields on dashboard for individual user
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    # Acts as the form while adding new user
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)

    