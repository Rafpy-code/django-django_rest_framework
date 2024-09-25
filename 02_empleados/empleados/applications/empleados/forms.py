from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'names', 
            'last_name', 
            'job', 
            'department',
            'image',
            'skills'
            ]
        
        widgets = {
            'names': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'job': forms.RadioSelect(attrs={'class': 'form-control'}),
            'department': forms.RadioSelect(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }