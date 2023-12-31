from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .form import ProfileForm
from .models import UserProfileModel
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.

# def store_file(file):
#     with open("temp\meena.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfileModel
    fields = "__all__"
    success_url = "/profiles"

class ListProfiles(ListView):
    template_name = "profiles/list_profiles.html"
    model = UserProfileModel
    context_object_name = "profiles"
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })
    
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             data = UserProfileModel(user_profile=request.FILES["user_file"])
#             data.save()
#             # store_file(request.FILES["user_file"])
#             return HttpResponseRedirect("/profiles")
#         else:
#             return render(request, "profiles/create_profile.html", {
#             "form": submitted_form
#         })