from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Veuillez indiquer le titre et l'auteur"
        self.fields['description'].label = "Formulez votre demande"
        self.fields['image'].required = False

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
        widgets = {
            'description': forms.Textarea(attrs={"class": "textarea", 'rows': '2'}),
        }