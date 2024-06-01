from django import forms

class PresentationForm(forms.Form):
    topic = forms.CharField(label='Enter Your Topic:', max_length=100)
    slide_number = forms.IntegerField(label='Enter Slide Number (5-25):', min_value=5, max_value=25)

