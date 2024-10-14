from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import UserAdminForm
from users.models import User


class CustomUserAdmin(UserAdmin):
    form = UserAdminForm

    list_display = ('email', 'full_name', 'phone', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'phone', 'avatar', 'country', 'email_verified', 'blocked')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    ordering = ['email']

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='managers').exists():
            return [field.name for field in self.model._meta.fields if field.name != 'blocked']
        return super().get_readonly_fields(request, obj)



if User in admin.site._registry:
    admin.site.unregister(User)


admin.site.register(User, CustomUserAdmin)
