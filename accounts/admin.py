from django.contrib import admin
from django.contrib.auth.models import Group
from unfold.admin import ModelAdmin
from accounts.forms import UserChangeForm, UserCreationForm
from accounts.models import User

@admin.register(User)
class UserAdmin(ModelAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'is_admin', 'is_active',)
    search_fields = ('username',)
    ordering = ('username',)
    list_filter = ('is_admin', 'is_active',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Status', {'fields': ('is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active',),
        }),
    )

    filter_horizontal = ()

# Unregister the default Group model from the admin
admin.site.unregister(Group)
