

from django.urls import path
from . import views  # import your views here

urlpatterns = [
    # Example endpoint
    path("", views.listings_list, name="listings-list"),  # e.g., GET /api/listings/
    path("<int:pk>/", views.listing_detail, name="listing-detail"),  # e.g., GET /api/listings/1/
]

    


