"""
User forms.
"""
# Internal Django Modules
from django import forms

class ProfileForms(forms.Form):
    """Profile form.
    """

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()