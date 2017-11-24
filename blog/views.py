from django.shortcuts import render

# Create your views here.

# from .models import Owner, Jamroom, OperatingHours, Customer, Booking
from blog.forms import HomeSearchForm

def home_search(request):
    search_term = "wydhrvdgwir3t532t7y"
    if request.method == "POST":
        MyHomeSearchForm = HomeSearchForm(request.POST)
        if MyHomeSearchForm.is_valid():
            search_term = MyHomeSearchForm.get("search_term", "")
    else:
        MyHomeSearchForm = HomeSearchForm()

    return render(request, 'blog/search_result.html', {"search_term" : search_term})
