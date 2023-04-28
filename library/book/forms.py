from django import forms
from author.models import Author


class SearchBooks(forms.Form):
    word = forms.CharField(
        label='Select book:',
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'style': "height: 2px; width: 100px; font-size:12px;"
            }
        ),
        required=False
    )




class BookForm(forms.Form):
    name = forms.CharField(max_length=128, required=True,
        widget= forms.TextInput(), label = 'Name')
    description = forms.CharField(max_length=256, required=True,
        widget= forms.TextInput(), label = 'Description')
    count = forms.IntegerField(required=True, 
        widget= forms.NumberInput(), label = 'Count')
    author = forms.ChoiceField(required=True,
        widget=forms.Select(), label = 'Select author')
    name.widget.attrs['class'] = "form-control form-control-lg"
    description.widget.attrs['class'] = "form-control form-control-lg"
    count.widget.attrs['class'] = "form-control form-control-lg"
    author.widget.attrs['class'] = "form-control form-control-lg"
 