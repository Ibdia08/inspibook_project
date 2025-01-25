from django.db import models

# Create your models here.
class Citation(models.Model):
    text = models.TextField()  # Texte de la citation
    author = models.CharField(max_length=100)  # Auteur de la citation
    created_at = models.DateTimeField(auto_now_add=True)  # Date d'ajout

    def __str__(self):
        return f'"{self.text}" - {self.author}'

