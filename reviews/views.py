from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse
# Create your views here.

# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()    
#         return render(request, "reviews/review.html", {
#         "form": form
#         })
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         else:
#             form = ReviewForm()    
#             return render(request, "reviews/review.html", {
#             "form": form
#             })
# class ReviewView(FormView): example
class ReviewView(CreateView):
    #CreateView saved data autimatically
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # This is used with FormView
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    

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

# class ThankYouView(View):
#     def get(self, request):
#         get_form_data_from_db = Review.objects.all().order_by('-id')[0]
#         print(get_form_data_from_db)
#         return render(request,"reviews/thank-you.html",
#                     {
#                     "form_db_data" : get_form_data_from_db
#                     })

# def thank_you(request):
#     get_form_data_from_db = Review.objects.all().order_by('-id')[0]
#     print(get_form_data_from_db)
#     return render(request,"reviews/thank-you.html",
#                   {
#                    "form_db_data" : get_form_data_from_db
#                   })

class ThankYouView(TemplateView):
    """
    This is specific TemplateView class for calling .html files 
    with in-built get method
    """
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        get_form_data_from_db = Review.objects.all().order_by('-id')[0]
        context_data = super().get_context_data(**kwargs)
        context_data["form_db_data"] = get_form_data_from_db
        return context_data

# class ReviewsListView(TemplateView):
#     template_name = "reviews/reviews_list.html"

#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         all_reviews_data = Review.objects.all()
#         context_data["reviews"] = all_reviews_data
#         return context_data

class ReviewsListView(ListView):
    template_name = "reviews/reviews_list.html"
    model = Review  #just pointer not instantiate  it
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data

# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context_data["review"] = selected_review
#         return context_data

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review # do not instantiate it

    def get_context_data(self, **kwargs: Any):
        context_data = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id = request.session.get("favourite_review")
        context_data["is_favourite"] = favourite_id == str(loaded_review.id) 
        return context_data
    
class AddFavouriteView(View):
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favourite_review"] = review_id
        print(request.session)
        redirect_url = reverse("single-view", args=[review_id])
        return HttpResponseRedirect(redirect_url)