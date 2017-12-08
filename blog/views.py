from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Owner, Jamroom, OperatingHours, Customer, Booking

from blog.forms import HomeSearchForm

def home_search(request):
    # search_result = "search_result wasn't initialised"
    # MyHomeSearchForm="MyHomeSearchForm wasn't initialised"
    if request.method == "POST":
        MyHomeSearchForm = HomeSearchForm(request.POST)
        if MyHomeSearchForm.is_valid():
            search_result = request.POST.get("search_term")
            # jamrooms = Jamroom.objects.all()
            # owners = Owner.objects.all()
            # for  jamroom in jamrooms:
            jamrooms = Jamroom.objects.filter(name__contains=search_result)
                # owners[i] = Owner.objects.filter(jamroom__owner_id__contains=jamroom.owner_id)
            owners = Owner.objects.filter(jamroom__name__contains=search_result)
            if jamrooms:
                return render(request, 'blog/search_result_display.html', {"jamrooms" : jamrooms, "owners" : owners})
        else:
            return render(request, 'blog/no_search_term.html')
    else:
        print("get triggered")
        MyHomeSearchForm = HomeSearchForm()
        return render(request, 'blog/home_search.html', {"MyHomeSearchForm" : MyHomeSearchForm})    # return render(request, 'blog/search_result.html', {"search_term" : search_term})

def list_all():
    return render( 'blog/list_all.html')

def book(request):
    print("shbd")
    return render(request, 'blog/book.html')

def booking_confirmed(request):
    # if request.method == "POST":
    #     customer = Customer.objects.filter


    return render(request, 'blog/booking_confirmed.html')

    # else:
    #     print("get triggered")
    #     MyHomeSearchForm = HomeSearchForm()
    #     return render(request, 'blog/home_search.html', {"MyHomeSearchForm" : MyHomeSearchForm})
