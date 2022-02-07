from django.shortcuts import render, redirect

# Create your views here.
def home_page(request):
    return render(request, "main/home_page.html", {})
