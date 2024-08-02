from django import forms 
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
         model = Profile
         fields = [
              'name',
              'email',
              'phone',
              'summary',
              'linkedin',
              'university',
              'work',
              'skill'
         ]