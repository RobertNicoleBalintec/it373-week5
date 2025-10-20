from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    
    def clean_title(self):
        t = self.cleaned_data['title']
        if "test" in t.lower():
            raise forms.ValidationError("Title cannot contain the word 'test'.")
        if len(t) < 3:
            raise forms.ValidationError('Title too short.')
        return t
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text'] 
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
