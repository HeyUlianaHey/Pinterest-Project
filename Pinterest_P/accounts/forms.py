from django import forms
from django.forms import ModelForm

from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'Введите имя пользователя'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'Введите пароль'}
        )
    )


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'Введите почту'}
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'Введите имя пользователя'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control rounded-pill', 'placeholder': 'Введите пароль'}
        )
    )


class EditProfileForm(ModelForm):
    photo = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['photo', 'about', 'fname', 'lname', 'pronouns', 'website']

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields["about"].widget.attrs["placeholder"] = "Расскажите свою историю"
        self.fields["fname"].widget.attrs["placeholder"] = "Введите имя"
        self.fields["lname"].widget.attrs["placeholder"] = "Введите фамилию"
        self.fields["pronouns"].widget.attrs["placeholder"] = "Введите имя пользователя"
        self.fields["website"].widget.attrs["placeholder"] = "Добавьте ссылку для привлечения трафика на свой сайт"

        for visible in self.visible_fields():
            if visible.name == 'about':
                visible.field.widget.attrs['class'] = 'edit-profile-input form-control about-input'
            else:
                visible.field.widget.attrs['class'] = 'edit-profile-input form-control rounded-pill'





