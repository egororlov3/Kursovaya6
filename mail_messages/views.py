import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import BlogPost
from .models import Client, Message, Mailing, MailingAttempt
from .forms import ClientForm, MessageForm, MailingForm, MailingAttemptForm


@method_decorator(cache_page(60 * 5), name='dispatch')
class MainView(ListView):
    model = Mailing
    template_name = 'mail_messages/main.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получение необходимой информации
        context['total_mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(is_active=True).count()
        context['unique_clients'] = Client.objects.values('email').distinct().count()

        # Получение трех случайных статей из блога
        random_articles = BlogPost.objects.all()
        context['random_articles'] = random.sample(list(random_articles),
                                                   min(len(random_articles), 3)) if random_articles.exists() else []

        return context


# ККЛИЕНТ
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'mail_messages/client_list.html'
    context_object_name = 'clients'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'mail_messages/client_detail.html'
    context_object_name = 'client'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self):
        return get_object_or_404(Client, id=self.kwargs.get('pk'))


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mail_messages/client_form.html'
    success_url = reverse_lazy('mail_messages:client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Автоматически устанавливаем владельца
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mail_messages/client_form.html'
    success_url = reverse_lazy('mail_messages:client_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        message = get_object_or_404(Client, id=self.kwargs.get('pk'))

        if message.owner != self.request.user:
            raise Http404()

        return message


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'mail_messages/client_confirm_delete.html'
    success_url = reverse_lazy('mail_messages:client_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        message = get_object_or_404(Client, id=self.kwargs.get('pk'))

        if message.owner != self.request.user:
            raise Http404()

        return message


# СООБЩЕНИЕ
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'mail_messages/message_list.html'
    context_object_name = 'messages'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'mail_messages/message_detail.html'
    context_object_name = 'message'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self):
        return get_object_or_404(Message, id=self.kwargs.get('pk'))


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mail_messages/message_form.html'
    success_url = reverse_lazy('mail_messages:message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mail_messages/message_form.html'
    success_url = reverse_lazy('mail_messages:message_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        message = get_object_or_404(Message, id=self.kwargs.get('pk'))

        if message.owner != self.request.user:
            raise Http404()

        return message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = 'mail_messages/message_confirm_delete.html'
    success_url = reverse_lazy('mail_messages:message_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        message = get_object_or_404(Message, id=self.kwargs.get('pk'))

        if message.owner != self.request.user:
            raise Http404()

        return message


# РАССЫЛКА
class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = 'mail_messages/mailing_list.html'
    context_object_name = 'mailings'


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = 'mail_messages/mailing_detail.html'
    context_object_name = 'mailing'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self):
        return get_object_or_404(Mailing, id=self.kwargs.get('pk'))


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mail_messages/mailing_form.html'
    success_url = reverse_lazy('mail_messages:mailing_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mail_messages/mailing_form.html'
    success_url = reverse_lazy('mail_messages:mailing_list')
    permission_required = 'mail_messages.can_disable_mailing'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        if not self.request.user.has_perm('mail_messages.can_disable_mailing'):
            return HttpResponse('У вас нет прав на отключение рассылки.', status=403)

        # Отключаем рассылку
        form.instance.is_active = False
        return super().form_valid(form)

    def get_object(self, queryset=None):
        message = get_object_or_404(Mailing, id=self.kwargs.get('pk'))

        if message.owner != self.request.user:
            raise Http404()

        return message


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = 'mail_messages/mailing_confirm_delete.html'
    success_url = reverse_lazy('mail_messages:mailing_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        message = get_object_or_404(Mailing, id=self.kwargs.get('pk'))

        if message.owner != self.request.user:
            raise Http404()

        return message


# ПОПЫТКА РАССЫЛКИ
class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = 'mail_messages/mailing_attempt_list.html'
    context_object_name = 'attempts'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingAttemptDetailView(LoginRequiredMixin, DetailView):
    model = MailingAttempt
    template_name = 'mail_messages/mailing_attempt_detail.html'
    context_object_name = 'attempt'

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingAttemptCreateView(LoginRequiredMixin, CreateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = 'mail_messages/mailing_attempt_form.html'
    success_url = reverse_lazy('mail_messages:mailing_attempt_list')


class MailingAttemptUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = 'mail_messages/mailing_attempt_form.html'
    success_url = reverse_lazy('mail_messages:mailing_attempt_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingAttemptDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingAttempt
    template_name = 'mail_messages/mailing_attempt_confirm_delete.html'
    success_url = reverse_lazy('mail_messages:mailing_attempt_list')

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)
