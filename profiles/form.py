from django import  forms 

class ProfileForm(forms.Form):
    user_file = forms.FileField()