from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name"]
        labels = {"name": ""}

        widgets = {"name": forms.Textarea(attrs={"cols": 80})}
