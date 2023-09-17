
from django import forms

class InputStringForm(forms.Form):
    input_string = forms.CharField(max_length=255)
