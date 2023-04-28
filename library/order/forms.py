from django import forms
from authentication.models import CustomUser
from book.models import Book
import datetime

class DateInput(forms.DateTimeInput):
    input_type = 'datetime-local' 
class OrderForm(forms.Form):
    user = forms.ChoiceField( required=True,
        label='Select User', widget=forms.Select())
    book = forms.ChoiceField( required=True,
        label='Select Book', widget=forms.Select())
    plated_end_at = forms.DateTimeField(widget=DateInput,
        label='Choose a time to return book:')
    user.widget.attrs['class'] = 'form-control'
    book.widget.attrs['class'] = 'form-control'
    plated_end_at.widget.attrs['max'] = '2025-01-01T00:00'
    current_time = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
    plated_end_at.widget.attrs['min'] = current_time
