from django.shortcuts import render

from .models import Owner, Jamroom, OperatingHours, Customer, Booking

from blog.forms import HomeSearchForm

def home_search(request):
    search_result = "search_result wasn't initialised"
    MyHomeSearchForm="MyHomeSearchForm wasn't initialised"
    if request.method == "POST":
        MyHomeSearchForm = HomeSearchForm(request.POST)
        if MyHomeSearchForm.is_valid():
            search_result = request.POST.get("search_term")
            search_result_display(search_result)
            return render(request, 'blog/home_search.html', {"MyHomeSearchForm" : MyHomeSearchForm})
            # return render(request, 'blog/search_result.html', {"search_result" : search_result})
    else:
        print("get triggered")
        MyHomeSearchForm = HomeSearchForm()
        return render(request, 'blog/home_search.html', {"MyHomeSearchForm" : MyHomeSearchForm})    # return render(request, 'blog/search_result.html', {"search_term" : search_term})

def search_result_display(search_result):
    
