from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
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

      