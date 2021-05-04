from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


ALL_in = 'All'
MECHANIC = 'Mechanic'
AUTOMATIC = 'Automatic'
ROBOTIC = 'Robotic'
TRANSMISSION = [
    (ALL_in, 'all'),
    (MECHANIC, 'mechanics'),
    (AUTOMATIC, 'automatic'),
    (ROBOTIC, 'robotic'),
]


class SearchForm(forms.Form):
    producer = forms.CharField(max_length=255, required=False)
    model = forms.CharField(max_length=255, required=False)
    release_year = forms.IntegerField(
        validators=[MinValueValidator(1920), MaxValueValidator(2020)], required=False
    )
    transmission = forms.ChoiceField(choices=TRANSMISSION, required=False, widget=forms.Select())
    color = forms.CharField(max_length=150, required=False)


class OneRowSearch(forms.Form):
    search = forms.CharField(max_length=255, required=False, label='')
