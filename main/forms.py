# forms.py
from django import forms
from .models import ToRegion

class ToRegionForm(forms.ModelForm):

    class Meta:
        model = ToRegion
        fields = '__all__'


