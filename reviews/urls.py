from django.urls import path
from . import views
# urlpatterns = [
#     path("",views.review),
#     path("thank-you", views.thank_you, name="thank")
# ]

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view(), name="thank"),
    path("reviews", views.ReviewsListView.as_view()),
    path("single-review/<int:pk>", views.SingleReviewView.as_view(), name="single-view")
]