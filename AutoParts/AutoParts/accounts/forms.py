from django import forms

from AutoParts.accounts.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('is_done', 'user',)
