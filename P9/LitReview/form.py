from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Veuillez indiquer le titre et l'auteur"
        self.fields['description'].label = "Formulez votre demande"
        self.fields['image'].required = True

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
        widgets = {
            'description': forms.Textarea(attrs={"class": "textarea", 'rows': '2'}),
        }

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['headline'].label = "Veuillez indiquer le titre et l'auteur"
        self.fields['rating'].label = "Note"
        self.fields['body'].required = True

    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        widgets = {
            'body': forms.Textarea(attrs={"class": "textarea", 'rows': '2'}),
        }
