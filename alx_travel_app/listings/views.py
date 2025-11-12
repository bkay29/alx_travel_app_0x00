
from django.http import JsonResponse

# Example view to list all listings
def listings_list(request):
    data = [
        {"id": 1, "name": "Beach House"},
        {"id": 2, "name": "Mountain Cabin"},
    ]
    return JsonResponse(data, safe=False)

# Example view to get a single listing by ID
def listing_detail(request, pk):
    # In real apps, you'd fetch from DB; here it's static for testing
    listings = {
        1: {"id": 1, "name": "Beach House"},
        2: {"id": 2, "name": "Mountain Cabin"},
    }
    listing = listings.get(pk)
    if listing:
        return JsonResponse(listing)
    return JsonResponse({"error": "Listing not found"}, status=404)

