from django import forms


class UserNewsEmailForm(forms.Form):
    email = forms.EmailField()