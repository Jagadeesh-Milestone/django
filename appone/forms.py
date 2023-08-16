from django import forms
from appone.models import student

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
print('hello world')
