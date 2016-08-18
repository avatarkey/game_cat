from django import forms
from .models import Game, Genre, Developer


class GameForm(forms.ModelForm):
	name = forms.CharField(
		label="Имя",
		max_length= 80,
		required=True)
	date = forms.DateField(
		widget=forms.TextInput(
			attrs={'type': 'date'}),
			required=False)        
	cover = forms.ImageField(
		required=False)
	developer = forms.ModelChoiceField(queryset=Developer.objects.all(),
		required=False)
	genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
		widget = forms.CheckboxSelectMultiple(),
		required=True)
	class Meta:
		model = Game
		fields = ('name', 'date', 'cover', 'developer', 'genre')