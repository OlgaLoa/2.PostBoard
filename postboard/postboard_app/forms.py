from django import forms
from .models import Post
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class PostForm(forms.ModelForm):
    class Meta:
        text_of_the_post = SummernoteTextFormField()
        model = Post

        fields = [
            'author_of_the_post',
            'category_of_the_post',
            'title_of_the_post',

    ]

