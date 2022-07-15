from django import forms
from .models import Ticket, Review, UserFollows
from ..accounts.views import User


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

class FollowForm(forms.ModelForm):
    def __init__(self, *args, username=None, following=None, followed_by=None,  **kwargs):
        super(FollowForm, self).__init__(*args, **kwargs)
        self.username = username
        self.following = following
        self.followed_by = followed_by
        self.fields['followed_user'].label = "Choisir parmi :"
        self.fields['followed_user'].queryset = User.objects.all().exclude(
            username=self.username).exclude(id__in=[f.followed_user.id for f in self.following])

    class Meta:
        model = UserFollows
        fields = ('followed_user',)
