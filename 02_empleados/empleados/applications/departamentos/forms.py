from django import forms

class NewDepartmentForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    nombre_corto = forms.CharField(max_length=50)