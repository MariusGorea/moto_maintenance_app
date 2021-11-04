from django import forms

from moto_app.models import Owner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields =  '__all__'
        exclude = ['user']


# class PartForm(forms.ModelForm):
#     class Meta:
#         model = Part
#         fields = '__all__'
#         exclude = ['']
