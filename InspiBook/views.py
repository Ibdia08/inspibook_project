from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Citation
from .forms import CitationForm
from django.db.models import Q  # Pour les recherches complexes
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib import messages



# Create your views here.


def home(request):
    return render(request, 'InspiBook/home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
            return redirect('login')  # Redirection après l'inscription
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'InspiBook/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('citations')
    else:
        form = AuthenticationForm()
    return render(request, 'InspiBook/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def citations(request):
    if request.method == 'POST':
        form = CitationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citations')
    else:
        form = CitationForm()
    citations = Citation.objects.all()
    return render(request, 'InspiBook/citations.html', {'form': form, 'citations': citations})


@login_required
def dashboard(request):
    citations = Citation.objects.filter(user=request.user)  # Récupérer les citations de l'utilisateur connecté
    return render(request, 'InspiBook/dashboard.html', {'citations': citations})


def recherche_citations(request):
    query = request.GET.get('q')  # Récupérer le mot-clé entré par l'utilisateur
    if query:
        citations = Citation.objects.filter(
            Q(text__icontains=query) | Q(author__icontains=query)
        )  # Recherche dans les champs 'text' et 'author'
    else:
        citations = Citation.objects.all()  # Retourner toutes les citations si aucune recherche
    return render(request, 'InspiBook/recherche.html', {'citations': citations, 'query': query})
 

@login_required
def editer_citation(request, id):
    citation = get_object_or_404(Citation, id=id, user=request.user)  # Vérifie que la citation appartient à l'utilisateur
    if request.method == 'POST':
        form = CitationForm(request.POST, instance=citation)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Retour au tableau de bord après modification
    else:
        form = CitationForm(instance=citation)
    return render(request, 'InspiBook/editer_citation.html', {'form': form, 'citation': citation})

@login_required
def supprimer_citation(request, id):
    citation = get_object_or_404(Citation, id=id, user=request.user)
    if request.method == 'POST':
        citation.delete()
        return redirect('dashboard')  # Retour au tableau de bord après suppression
    return render(request, 'InspiBook/supprimer_citation.html', {'citation': citation})
