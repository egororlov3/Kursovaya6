from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client, Message, Mailing, MailingAttempt
from .forms import ClientForm, MessageForm, MailingForm, MailingAttemptForm


# ККЛИЕНТ
class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')


# СООБЩЕНИЕ
class MessageListView(ListView):
    model = Message
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = Message
    template_name = 'message_detail.html'
    context_object_name = 'message'


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('message_list')


# РАССЫЛКА
class MailingListView(ListView):
    model = Mailing
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'message_detail.html'
    context_object_name = 'message'


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('message_list')


# ПОПЫТКА РАССЫЛКИ
class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'message_list.html'
    context_object_name = 'messages'


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    template_name = 'message_detail.html'
    context_object_name = 'message'


class MailingAttemptCreateView(CreateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MailingAttemptUpdateView(UpdateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = 'message_form.html'
    success_url = reverse_lazy('message_list')


class MailingAttemptDeleteView(DeleteView):
    model = MailingAttempt
    template_name = 'message_confirm_delete.html'
    success_url = reverse_lazy('message_list')
