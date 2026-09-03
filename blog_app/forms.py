from django import forms
from django.core.validators import ValidationError
from blog_app.models import Message


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='Your name')
    text = forms.CharField(max_length=10, label='Your Message')
    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name cannot be the same as text', code='name_text_same')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter your name',
                                           "style": "max-width: 50%"}),
            "family": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter your family',
                                           "style": "max-width: 50%"}),
            "email": forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter your email',
                                           "style": "max-width: 50%"}),
            "age": forms.TextInput(attrs={'class': 'form-control',
                                           "style": "max-width: 10%"}),
            "text": forms.Textarea(attrs={'class': 'form-control',})
        }