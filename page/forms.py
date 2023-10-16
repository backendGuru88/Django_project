from django import forms

class SignUpForm(forms.Form):
    # Define form fields here
    field1 = forms.CharField(label='Field 1', max_length=100)
    field2 = forms.EmailField(label='Email')
    # Add more fields as needed
  