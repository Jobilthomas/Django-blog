from .models import Comment
from django import forms

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "email": "email Id",
            "comment": "Your comment"
        }
        error_messages = {
            "user_name": {
                "required": "Your name field should be filled",
                "max_length": "Name is too long"
            },
            "email": {
                "required": "email Id field should be filled",
                "max_length": "email Id is too long"
            },
            "comment": {
                "required": "You haven't written any comment",
                "max_length": "Your comment is too long"
            }
        }