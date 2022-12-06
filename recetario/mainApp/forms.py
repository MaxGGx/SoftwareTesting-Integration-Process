from django import forms
from .models import *

class RecetaForm(forms.ModelForm):
    class Meta:
        model = receta
        fields = ["nombreReceta", "ingredientes", "pasos", "imagenReceta", "autor"]
        widgets= {
            "nombreReceta":forms.TextInput(attrs={"class":"form-control"}),
            "ingredientes":forms.Textarea(attrs={"class":"form-control"}),
            "pasos":forms.Textarea(attrs={"class":"form-control"}),
            "imagenReceta":forms.FileInput(attrs={"class":"form-control"}),
            "autor":forms.TextInput(attrs={"class":"form-control"}),
        }
