from django import forms
from .models import ImageModel , Comment
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Comment here!'})

        }
        labels = {'text':""}