from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20, required=True,
                               widget=forms.TextInput(attrs={
                                   "placeholer": "Username",
                                   "required": True,
                                   "name": "username"
                               })
                               )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "name": "password",
            "required": True
        })
    )
    password_confirmation = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(attrs={
            "placeholder": "Repeat Password",
            "name": "password_confirmation",
            "required": True
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placheholder": "email",
            "name": "email",
            "required": True
        }
        )
    )

    image = forms.ImageField()

    def clean_username(self):
        username = self.cleaned_data["username"]
        is_username_taken = User.objects.filter(username=username).exists()

        if is_username_taken:
            raise forms.ValidationError("Username is already taken")

        return username

    def clean(self):
        data = super().clean()
        password = data["password"]
        password_confirmation = data["password_confirmation"]

        if password != password_confirmation:
            raise forms.ValidationError("Password do not match")
        return data

    def save(self):
        data = self.cleaned_data
        print(data)
        image = data["image"]
        data.pop("password_confirmation")
        data.pop("image")
        user = User.objects.create_user(**data)
        profile = Profile(user=user, image=image)
        profile.save()

