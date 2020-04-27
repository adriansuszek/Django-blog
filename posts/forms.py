from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    comment_content = forms.CharField(widget=forms.Textarea(attrs={ #this will overwrite layout of class Meta: fields = ['comment_content']
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '5'
    }))
    class Meta:
        model = Comment
        fields = ['comment_content']
