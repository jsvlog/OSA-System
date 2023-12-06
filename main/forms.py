# forms.py
from django import forms
from .models import ToRegion, FromRegion

class ToRegionForm(forms.ModelForm):

    class Meta:
        model = ToRegion
        fields = '__all__'

class FromRegionForm(forms.ModelForm):

    class Meta:
        model = FromRegion
        fields = '__all__'
