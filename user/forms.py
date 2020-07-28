from django import forms
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(label = "Username")
    password = forms.CharField(label = "Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "User Name")
    email = forms.EmailField(label= 'E-mail')
    password = forms.CharField(max_length=20,label = "Password",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label ="Confirm Password",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email = self.cleaned_data.get('email')

        if password and confirm and password != confirm:
            raise forms.ValidationError("Incorrect Password")

        values = {
            "username" : username,
            "password" : password,
            "email" : email
        }
        return values


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [ "name", "profile_picture","gender","about"]
