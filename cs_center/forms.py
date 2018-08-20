from django import forms
from .models import Post

CHOICES =(
    ("동의", "반대")
)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        profile = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


