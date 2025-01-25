from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='deconnexion'),
    path('citations/', views.citations, name='citations'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('citations/', views.liste_citations, name='listes_citations'),
    path('recherche/', views.recherche_citations, name='recherche'),
    path('citation/<int:id>/edit/', views.editer_citation, name='editer_citation'),
    path('citation/<int:id>/delete/', views.supprimer_citation, name='supprimer_citation'),

]
