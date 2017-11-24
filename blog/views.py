from django.shortcuts import render

# Create your views here.

def home_search(request):
    return render(request, 'blog/home_search.html')
