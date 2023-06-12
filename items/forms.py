from django import forms
from django.core import validators
from items.models import Theme

class CreateItemForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-field name'}), label='Nombre')
	description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", 'class':'form-field description'}), label='Descripción', required=True)

	choices = (
		('Mods', 'Mods'),
		('Guias', 'Guias'),
		('Reviews', 'Reviews')
	)
	category = forms.ChoiceField(required=True, choices = choices, widget=forms.Select(attrs={'class':'form-field select'}), label='Categoría')
	
	theme = forms.ModelChoiceField(queryset=Theme.objects.all(), widget=forms.Select(attrs={'class':'form-field select'}), label='Tema')
	images = forms.ImageField(label='Subir imagenes', widget=forms.ClearableFileInput(attrs={'multiple':True, 'name':'images', 'class':'form-field upload'}))
	files = forms.FileField(label='Subir archivos',required=False, widget=forms.ClearableFileInput(attrs={'multiple':True, 'name':'files', 'class':'form-field upload'}))