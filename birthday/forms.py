from django import forms
from .models import wishes

class wishesform(forms.ModelForm):
    class Meta:
        model=wishes
        fields='__all__'
