from django import forms
from django.forms import ModelForm, TextInput
from .models import Todo 


class CreateTodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            
        }