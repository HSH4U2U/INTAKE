from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'      # 여기 content와 star만 들어가게 나머지는 알아서 값 넣을 수 있도록 구현
