from django import forms
from blog_site_backend.models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
