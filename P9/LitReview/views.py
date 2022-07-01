import flux as flux
from django.views.generic import (DetailView)
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import TicketForm, ReviewForm
from .models import Ticket, Review
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from itertools import chain
from django.db.models import CharField, Value


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

class TicketFormView(FormView):
    template_name = 'LitReview/creat_ticket.html'
    form_class = TicketForm
    success_url = '/'

    def form_valid(self, form):
        Ticket.objects.create(**form.cleaned_data, user=self.request.user)
        print(form.cleaned_data)
        return super().form_valid(form)


def create_review(request):


    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            ticket_form.cleaned_data["user"] = request.user
            ticket = Ticket.objects.create(**ticket_form.cleaned_data)
            review_form.cleaned_data["user"] = request.user
            review_form.cleaned_data["ticket"] = ticket
            Review.objects.create(**review_form.cleaned_data)
            return redirect('/')
        else:
            return render(request, 'LitReview/ticket_review.html', {"ticket_form":ticket_form, "review_form":review_form} )
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
        return render(request, 'LitReview/ticket_review.html', {"ticket_form":ticket_form, "review_form":review_form} )

class PostListView(ListView):
    template_name = 'LitReview/flux.html'
    model = Ticket
    paginate_by = 100

    def get_queryset(self):
        reviews = Review.objects.filter(user=self.request.user)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        tickets = Ticket.objects.filter(user=self.request.user)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        return sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )


