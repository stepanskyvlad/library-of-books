from django import forms


class LogInForm(forms.Form):
    email = forms.EmailField(
        label='Enter your email',
        widget=forms.EmailInput(
            attrs={
                'class': "form-control form-control-lg"
            }
        )
    )

    password = forms.CharField(
        label='Enter your password',
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control form-control-lg"
            }
        )
    )


class SignInForm(forms.Form):

    ROLE_CHOICES = (
        (0, 'visitor'),
        (1, 'librarian'),
    )

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(
            attrs={
                'class': "form-control form-control-lg"
            }
        )
    )
    middle_name = forms.CharField(
        label="Middle name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg"
            }
        )
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg"
            }
        )
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-lg"
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg"
            }
        )
    )
    role = forms.ChoiceField(
        label="Role",
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input"
            }
        )
    )
