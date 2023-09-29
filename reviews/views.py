from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()    
        return render(request, "reviews/review.html", {
        "form": form
        })
    
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        else:
            form = ReviewForm()    
            return render(request, "reviews/review.html", {
            "form": form
            })



# def review(request):
#     if request.method == "POST":
#         # entered_username = request.POST["user_name"]
#         # print(entered_username)
#         # return HttpResponseRedirect("/thank-you")
#         # to update existing row
#         # existing_row = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST, instance=existing_row)
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # If you are not using ModelForm
#             # valid_form_data = Review(user_name= form.cleaned_data['user_name'],
#             #        review_text = form.cleaned_data['review'],
#             #        rating = form.cleaned_data['rating'])
#             # valid_form_data.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()    
#     return render(request, "reviews/review.html", {
#     "form": form
#     })

def thank_you(request):
    get_form_data_from_db = Review.objects.all().order_by('-id')[0]
    print(get_form_data_from_db)
    return render(request,"reviews/thank-you.html",
                  {
                   "form_db_data" : get_form_data_from_db
                  })