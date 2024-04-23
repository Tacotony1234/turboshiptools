from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100)
    address1 = forms.CharField(label='Address line 1', max_length=255)
    address2 = forms.CharField(label='Address line 2', max_length=255, required=False)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(label='Zip Code', max_length=12)
    country = forms.CharField(max_length=100)
    # Payment details are handled by the payment gateway
