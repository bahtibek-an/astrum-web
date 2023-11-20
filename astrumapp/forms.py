from django import forms


class NameForm(forms.Form):
    full_name = forms.CharField(label="full_name", max_length=100)
    phone = forms.CharField(label="phone", max_length=100)
    nick_name = forms.CharField(label="nick_name", max_length=100)

class ConfirmForm(forms.Form):
    phone = forms.CharField(label="phone", max_length=20)
    code = forms.CharField(label="code", max_length=5)
    full_name = forms.CharField(label="full_name", max_length=100)
    nick_name = forms.CharField(label="nick_name", max_length=100)
