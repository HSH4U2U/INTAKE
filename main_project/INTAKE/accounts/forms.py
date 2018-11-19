from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
import re


# def user_validator(value):
#     if len(value) < 5:
#         raise forms.ValidationError('5글자 이상 입력해주세요.')
#     if ('!', '~', '#', '$', '%', '^', '&', '*', '(', ')') in value:
#         raise forms.ValidationError('문자, 숫자, @/./+/-/_만 입력이 가능합니다.')


def phone_validator(value):
    number_str = value.strip('-')
    pattern = "^01[016789][1-9]\\d{6,7}$"
    if not re.match(pattern, number_str):
        raise forms.ValidationError('휴대폰 번호를 다시 입력해주세요')


class SignupForm(UserCreationForm):
    # phone = forms.CharField(validators=[phone_validator])
    phone = forms.CharField()
    address = forms.CharField(max_length=100)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )

    def save(self):
        user = super().save()

        Profile.objects.create(
            user=user,
            phone=self.cleaned_data['phone'],
            address=self.cleaned_data['address'],
        )
        return user