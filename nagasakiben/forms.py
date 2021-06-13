from django import forms
from .models import Dictionary, Feedback, Post, Comment

class DictionaryForm(forms.ModelForm):

    class Meta:
        model = Dictionary
        fields = ('word', 'pronunciation', 'meaning', 'usage',)

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('written_by', 'feedback_content',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('written_by', 'content',)
