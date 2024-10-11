from django import forms
from .models import Client, Message, Mailing, MailingAttempt


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'


class MailingAttemptForm(forms.ModelForm):
    class Meta:
        model = MailingAttempt
        fields = '__all__'
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
