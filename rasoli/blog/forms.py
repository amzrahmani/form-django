from django import forms

class create_form(forms.Form):
    title = forms.CharField(required=False )
    body =forms.CharField(label="TEXT")
    create= forms.DateField()