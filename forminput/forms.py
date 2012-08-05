from django import forms
from forminput.models import Band

class BandForm(forms.ModelForm):
    class Meta:
        model = Band

