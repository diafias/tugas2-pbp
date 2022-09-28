from django import forms
from todolist.models import Task

class Input_Form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
    
    