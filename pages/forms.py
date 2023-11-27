# forms.py
from django import forms

class YourModelSearchForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    # Add other fields as needed
