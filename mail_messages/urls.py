from django.urls import path
from .views import (
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView,
    MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView,
    MailingAttemptListView, MailingAttemptDetailView, MailingAttemptCreateView, MailingAttemptUpdateView,
    MailingAttemptDeleteView,
)

urlpatterns = [
    # КЛИЕНТ
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    # СООБЩЕНИЕ
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    # РАССЫЛКА
    path('mailing/', MailingListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),

    # ПОПЫТКА РАССЫЛКИ
    path('mailing-attempt/', MailingAttemptListView.as_view(), name='mailing-attempt_list'),
    path('mailing-attempt/<int:pk>/', MailingAttemptDetailView.as_view(), name='mailing-attempt_detail'),
    path('mailing-attempt/create/', MailingAttemptCreateView.as_view(), name='mailing-attempt_create'),
    path('mailing-attempt/<int:pk>/update/', MailingAttemptUpdateView.as_view(), name='mailing-attempt_update'),
    path('mailing-attempt/<int:pk>/delete/', MailingAttemptDeleteView.as_view(), name='mailing-attempt_delete'),
]
