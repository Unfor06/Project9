from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import TicketDetailView, TicketFormView, create_review, PostListView
from .views import index

urlpatterns = [
    path('', index, name='accueil'),
    path('accueil/<valeur>/', index, name='accueil'),
    path('ticket/<pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('createticket/', TicketFormView.as_view(), name='creat_ticket'),
    path('createreview/', create_review, name='create_review'),
    path('flux/', PostListView.as_view(), name='post'),
    ]