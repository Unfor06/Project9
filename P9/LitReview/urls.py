from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import TicketDetailView, TicketFormView, create_review, PostListView, FollowView, FollowDeleteView, feed, ModifTicket, TicketDelete, PostDelete, ModifPost
from .views import index

urlpatterns = [
    path('', feed, name='accueil'),
    path('accueil/<valeur>/', feed, name='accueil'),
    path('ticket/<pk>/', TicketDetailView.as_view(), name='ticket-detail'),
    path('ticket/create', TicketFormView.as_view(), name='creat_ticket'),
    path('createreview/', create_review, name='create_review'),
    path('flux/', feed, name='post'),
    path("follow/", FollowView.as_view(), name="abonnements"),
    path("unfollow/<pk>/delete/", FollowDeleteView.as_view(), name="unfollow-delete"),
    path("", feed, name="flux"),
    path("post/",PostListView.as_view(),name="posts"),
    path("tikcet/<pk>/update",ModifTicket.as_view(),name="modifier_ticket"),
    path("ticket/<pk>/delete",TicketDelete.as_view(), name='supprimer_ticket'),
    path("post/<pk>/delete",PostDelete.as_view(), name='supprimer_post'),
    path("post/<pk>/update",ModifPost.as_view(), name= 'modifier_post'),
    ]