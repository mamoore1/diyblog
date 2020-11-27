import datetime
from django import forms


class NewCommentForm(forms.Form):
    """Form for adding new comments"""
    comment_text = forms.CharField(max_length=1000, help_text="Enter your comment", widget=forms.Textarea)

    def clean_comment_text(self):
        data =  self.cleaned_data['comment_text']
        return data
