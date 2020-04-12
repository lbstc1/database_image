from django import forms
from.models import stu

class stu_form(forms.ModelForm):
    class Meta:
        model=stu
        fields='__all__'
