from django import forms

class NewAuthor(forms.Form):
    first_name = forms.CharField(max_length=20, required=True,
        widget= forms.TextInput())
    last_name = forms.CharField(max_length=20, required=True,
        widget= forms.TextInput())
    patronymic = forms.CharField(max_length=20, required=False,
        widget= forms.TextInput())
    # submit = forms.
    first_name.widget.attrs['class'] = "form-control form-control-lg"
    last_name.widget.attrs['class'] = "form-control form-control-lg"
    patronymic.widget.attrs['class'] = "form-control form-control-lg"
