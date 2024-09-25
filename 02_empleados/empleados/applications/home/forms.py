from django import forms
from .models import PruebaBBDD

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""
        model = PruebaBBDD
        fields = (
            'titulo',
            'subtitulo',
            'cantidad'
        )
        widgets = {
        'titulo': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Titulo',
                }),
        'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
        'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
    }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 0:
            raise forms.ValidationError('La cantidad no puede ser negativa')
        return cantidad
    

