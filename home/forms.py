from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FeatureRequestForm(forms.Form):
    """
    A form for users to submit feature requests.
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
        label='Your Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
        label='Your Email'
    )
    feature_title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Feature Title', 'class': 'form-control'}),
        label='Feature Title'
    )
    feature_description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Describe the feature...', 'class': 'form-control', 'rows': 5}),
        label='Feature Description'
    )
    category = forms.ChoiceField(
        choices=[
            ('', 'Select a Category'),  # Add a default option
            ('engineering', 'Engineering Surveying'),
            ('mining', 'Mining Surveying'),
            ('topographic', 'Topographic Surveying'),
            ('remote_sensing', 'Remote Sensing'),
            ('general', 'General'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Surveying Category'
    )
    urgency = forms.ChoiceField(
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Urgency'
    )
    agree_to_terms = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='I agree to the terms and conditions.' # Add a label
        )


    def clean_email(self):
        """
        Custom validation for the email field.
        """
        email = self.cleaned_data.get('email')
        # Add any custom email validation logic here (e.g., check for duplicates)
        return email
    
    def clean_agree_to_terms(self):
        """
        Custom validation to ensure the user agrees to the terms.
        """
        agree = self.cleaned_data.get('agree_to_terms')
        if not agree:
            raise ValidationError(_("You must agree to the terms and conditions."))
        return agree