from django.shortcuts import render

# Create your views here.

# from .models import Owner, Jamroom, OperatingHours, Customer, Booking
from blog.forms import HomeSearchForm

def home_search(request):
    search_term = "wydhrvdgwir3t532t7y"
    MyHomeSearchForm="db5f61g8yh87d4675fb76g"
    if request.method == "POST":
        print("triggered")
        MyHomeSearchForm = HomeSearchForm(request.POST)
        if MyHomeSearchForm.is_valid():
            # search_term = MyHomeSearchForm.g
    # return response(request, 'blog/search_result.html' , { 'search_term': search_term})
            return render(request, 'blog/search_result.html', {"search_term" : search_term})
    else:
        MyHomeSearchForm = HomeSearchForm()
        # search_term = request.POST['search_term']
        return render(request, 'blog/home_search.html')    # return render(request, 'blog/search_result.html', {"search_term" : search_term})

# def search_result(request):


    # return render(request, 'blog/search_result.html' , { 'search_term': search_term})    # return render(request, 'blog/search_result.html', {"search_term" : search_term})
