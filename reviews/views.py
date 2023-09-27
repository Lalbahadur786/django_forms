from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
# Create your views here.

def review(request):
    if request.method == "POST":
        # entered_username = request.POST["user_name"]
        # print(entered_username)
        # return HttpResponseRedirect("/thank-you")
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()    
    return render(request, "reviews/review.html", {
    "form": form
    })

def thank_you(request):
    return render(request,"reviews/thank-you.html")