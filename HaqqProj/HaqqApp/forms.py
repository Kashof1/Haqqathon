from django import forms
from .models import Employer, Refugee

class EmployerSignUpForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['first_name', 'last_name', 'email']


class RefugeeSignUpForm(forms.ModelForm):

    class Meta:
        model = Refugee
        fields = ['first_name', 'last_name', 'age', 'skills']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make the 'skills' field read-only
        self.fields['skills'].widget.attrs['readonly'] = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.skills = self.cleaned_data.get('skills', '')
        if commit:
            instance.save()
        return instance

class SkillSearchForm(forms.Form):
    skill = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly': 'readonly', 'placeholder': 'Enter skill to search'}))