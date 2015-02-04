from django import forms

class AddContent(forms.Form):
    link = forms.CharField(label='Link to IMDb Page (Movie or Show)')