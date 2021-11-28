from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User

from .models import users

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput)
    password2=forms.CharField(label='Password confirmation',widget=forms.PasswordInput)
    class Meta:
        model=users
        fields=('id',)
        def clean_password2(self):
            password1=self.cleaned_data.get("password1")
            password2=self.cleaned_data.get("password2")
            if password1 and password2 and password1!=password2:
                raise forms.ValidationError("Passwords don't match")
            return password2
        def save(self,commit=True):
            user=super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=users
        fields=('id','lockernum','department','name','is_active','is_admin')
    def clean_password(self):
        return self.initial["password"]