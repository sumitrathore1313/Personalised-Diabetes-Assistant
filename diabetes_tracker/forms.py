from django import forms
from . models import Glucose

class Entry(forms.ModelForm):
    class Meta:
        model = Glucose
        fields = ('glucose', 'sleep', 'weight', 'duration_of_exercise', 'type_of_exercise')
