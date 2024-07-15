from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """Form for Blog Post data"""
    class Meta:
        """provide metadata about the form"""
        model = Post
        fields = ('title', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,  # Specifies the height
            'cols': 40,  # Specifies the width
            'placeholder': 'Enter your text here...'
        })
        }      