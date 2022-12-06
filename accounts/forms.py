from django import forms
from django.contrib.auth.models import User

class PasswordResetForm(forms.Form):

    username = forms.CharField(widget= forms.TextInput(attrs={
        'class':'form-control',
        'autocomplete':'off'
    }))

    email = forms.EmailField(widget= forms.TextInput(attrs={
        'class':'form-control',
        'type':'email',
        'autocomplete':'off'
    }))

    def clean(self):
        cleaned = super().clean()

        if not User.objects.filter(username=cleaned['username']).exists():
            raise forms.ValidationError('El usuario no existe')
        
        if not User.objects.filter(email=cleaned['email']).exists():
            raise forms.ValidationError('El correo electronico no existe')

        return cleaned

    def get_user(self):

        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)


class ChangePasswordForm(forms.Form):

    password = forms.CharField(widget= forms.PasswordInput(attrs= {
        'class':'form-control',
        'placeholder':'Nueva contraseña',
        'autocomplete':'off'
    }))

    confirmPassword = forms.CharField(widget= forms.PasswordInput(attrs= {
        'class':'form-control',
        'placeholder':'Confirme su contraseña',
        'autocomplete':'off'
    }))

    def clean(self):

        cleaned = super().clean()

        password = cleaned['password']
        confirmPassword = cleaned['confirmPassword']

        if password != confirmPassword:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned