from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt
from .forms import MailingAdminForm

admin.site.register(Client)
admin.site.register(Message)
admin.site.register(MailingAttempt)


class MailingAdmin(admin.ModelAdmin):
    form = MailingAdminForm

    def get_readonly_fields(self, request, obj=None):
        """
        Если пользователь является менеджером, делаем все поля кроме is_active доступными только для чтения.
        """
        if request.user.groups.filter(name='managers').exists():
            return [field.name for field in self.model._meta.fields if field.name != 'is_active']
        return super().get_readonly_fields(request, obj)


admin.site.register(Mailing, MailingAdmin)
