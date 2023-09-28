from django import forms

class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=20,error_messages={"required": "You Name should not be empty",
                   "max_length": "Please provide shorter name"})
    review = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)