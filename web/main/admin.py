from allauth.account.models import EmailAddress
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from userprofile.admin import ProfileInline

User = get_user_model()


class EmailsInline(admin.TabularInline):
    """Class for inherit emails table to UserAdmin"""
    model = EmailAddress
    can_delete = False
    extra = 1

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False if obj else True


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('-id',)
    list_display = ('email', 'full_name', 'is_active', 'email_verified')
    inlines = (EmailsInline, ProfileInline)

    fieldsets = (
        (_('Personal info'), {'fields': ('id', 'first_name', 'last_name', 'email', 'birthday', 'gender')}),
        (_('Secrets'), {'fields': ('password',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('id',)


title = settings.MICROSERVICE_TITLE

admin.site.site_title = title
admin.site.site_header = title
admin.site.site_url = '/'
admin.site.index_title = title

admin.site.unregister(Group)
