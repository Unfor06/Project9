import flux as flux
from django.views.generic import (DetailView)
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ticket, Review
from django.views.generic.list import ListView

def index(request, valeur="bienvenue sur LitReview"):
    return render(request=request,template_name="LitReview/index.html", context={'valeur':valeur,'tickets':Ticket.objects.all()})

class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    extra_context = {'reviews': Review.objects.all()}

class FluxListView(ListView, LoginRequiredMixin):
        model = Ticket
        paginate_by = 100

        def get_queryset(self):
            filter_val = self.request.user('filter', 'give-default-value')
            order = self.request.user('orderby', 'give-default-value')
            new_context = Ticket.objects.filter(
                state=filter_val,
            ).order_by(order)
            return new_context
