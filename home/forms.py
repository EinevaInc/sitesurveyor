from django import forms
from .models import FeatureRequest
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['name', 'email', 'feature_title', 'feature_description', 'category', 'urgency', 'agree_to_terms']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
            'feature_title': forms.TextInput(attrs={'placeholder': 'Feature Title', 'class': 'form-control'}),
            'feature_description': forms.Textarea(attrs={'placeholder': 'Describe the feature...', 'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'urgency': forms.Select(attrs={'class': 'form-select'}),
            'agree_to_terms': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'feature_title': 'Feature Title',
            'feature_description': 'Feature Description',
            'category': 'Surveying Category',
            'urgency': 'Urgency',
            'agree_to_terms': 'I agree to the terms and conditions.',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

    def clean_agree_to_terms(self):
        agree = self.cleaned_data.get('agree_to_terms')
        if not agree:
            raise ValidationError(_("You must agree to the terms and conditions."))
        return agree