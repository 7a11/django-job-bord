from django import forms

from .models import applyy , Job


class applyyform(forms.ModelForm):
    class Meta:
        model = applyy
        fields = ['name','email','website','cv','cover_letter']

class jobform(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug','owner') # show all objects without slug