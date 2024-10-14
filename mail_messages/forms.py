from django import forms
from .models import Client, Message, Mailing, MailingAttempt


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'full_name', 'comment']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'body']


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['title', 'start_datetime', 'periodicity', 'status', 'message', 'clients', 'is_active']


class MailingAttemptForm(forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = '__all__'
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MailingAdminForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['is_active']

