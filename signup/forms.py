from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Username',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Email',
        })
        self.fields['password1'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Repeat Password'
        })

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'placeholder' : 'Username'
                                }))
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class' : 'form-control',
                                    'placeholder' : 'Email'
                            }))

    class Meta:
        model = User
        fields = ['username', 'email']
