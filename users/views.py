from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistrationForm, UserProfileForm
from .models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register')  # Замените 'home' на нужный маршрут

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Генерация письма с подтверждением
        current_site = get_current_site(self.request)
        mail_subject = 'Активируйте свой аккаунт'
        message = render_to_string('users/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })

        try:
            send_mail(
                mail_subject,
                message,
                'sidxxx3@yandex.ru',
                [user.email],
                fail_silently=False,
            )

            messages.success(self.request,
                             'На ваш email отправлено письмо для активации аккаунта. Пожалуйста, проверьте почту.')

        except Exception as e:
            return self.form_invalid(form)

        return super().form_valid(form)  # Завершение обработки и перенаправление на success_url


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


# Верификация email
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('users:login')
    else:
        return render(request, 'users/activation_invalid.html')
