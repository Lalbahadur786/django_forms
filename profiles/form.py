from django import  forms 

class ProfileForm(forms.Form):
    # user_file = forms.FileField()
    user_file = forms.ImageField()