from django import forms


class UserQuestionForm(forms.Form):
    issue = forms.CharField(max_length=250)
    child_name = forms.CharField(max_length=150)
    child_age = forms.IntegerField(min_value=2, max_value=20)
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)
    desc = forms.Textarea()