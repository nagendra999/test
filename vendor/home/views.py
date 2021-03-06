from django.shortcuts import render

# import forms & models
from .forms import SignUpForm
from .models import Customers


# Create your views here.


def home(request):
    return render(request, 
		  'home.html' )
	

def base(request):
    return render(request,
                  'base.html',)


def faq(request):
    return render(request,
                  'faq.html',)
def signup(request):
    if request.method == "GET":
        return render(request,
                      'signup.html',
                      {'form' : SignUpForm})
    elif request.method == "POST":
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request,
                          'signup.html',
                          { 'form' : form }, )
        else:
            Customers.objects.create(
                    first_name = form.cleaned_data["first_name"],
                    last_name = form.cleaned_data["last_name"],
                    company = form.cleaned_data["company"],
                    email_id = form.cleaned_data["email_id"],
                    password = form.cleaned_data["password"],
                    phone_no = form.cleaned_data["phone_no"],
                    website = form.cleaned_data["website"],
                    )
            return render(request,
                          'signup_complete.html',)


def profile(request):
    return render(request,
                 'profile.html',)

