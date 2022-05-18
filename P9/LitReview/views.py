from django.views.generic import (DetailView)
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket, Review

def index(request, valeur="bienvenue sur LitReview"):
    return render(request=request,template_name="LitReview/index.html", context={'valeur':valeur})

class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    extra_context = {'reviews': Review.objects.all()}
