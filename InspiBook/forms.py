from django import forms
from .models import Citation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CitationForm(forms.ModelForm):
    class Meta:
        model = Citation
        fields = ['text', 'author']

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author:
            raise forms.ValidationError("Le champ 'Auteur' est obligatoire.")
        return author

class CustomUserCreationForm(UserCreationForm):
    nom = forms.CharField(max_length=100, required=True, label="Nom")
    prenom = forms.CharField(max_length=100, required=True, label="Prénom")
    numero_telephone = forms.CharField(max_length=15, required=True, label="Numéro de téléphone")

    class Meta:
        model = User
        fields = ['username', 'nom', 'prenom', 'numero_telephone', 'password1', 'password2']
