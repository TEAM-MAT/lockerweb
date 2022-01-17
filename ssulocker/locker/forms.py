from ast import ImportFrom
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db.models.enums import Choices
from django.forms.widgets import Widget

from .models import lockers, users

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={
        'required':'True'
    }))
    password2=forms.CharField(
        label='Password confirmation',widget=forms.PasswordInput(attrs={'required':'True',
        'placeholder': ('Password confirmation')
        }
        )
    )

    class Meta:
        model=users
        fields=('id','department','name','phone')
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
        fields=('id','department','name','phone','is_active','is_admin')
    def clean_password(self):
        return self.initial["password"]


class lockeraddForm(forms.ModelForm):
    buildings=(('HN','형남공학관'),('IS','정보과학관'),('CB','문화관'))
    building=forms.ChoiceField(label="building",widget=forms.MultipleChoiceField,choices=buildings)
    written_lockernum=forms.CharField(label="lockernumwritten",widget=forms.CharField)
    floor=forms.IntegerField(label="floor",widget=forms.IntegerField)
    sector=forms.CharField(label="sector",widget=forms.CharField)
    departments=(('CS','컴퓨터학부'),
    ('GM','글로벌미디어학부'),('EIE','전자정보공학부'),('SW','소프트웨어학부'),
    ('AIC','AI융합학부'))
    department=forms.ChoiceField(label="department",widget=forms.ChoiceField(choices=departments))
    res=((0,'빈사물함'),(1,'예약된사물함'))
    reserved=forms.ChoiceField(label="예약여부",choices=res)
    class Meta:
        model=lockers
        fields=('building','written_lockernum','floor','sector','department','reserved')
    def save(self,commit=True):
        l=super().save(commit=False)
        l.lockernum=str(l.building)+str(l.floor)+str(l.sector)+str(l.written_lockernum)
        if commit:
            l.save()