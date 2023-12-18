from django.shortcuts import render, redirect
from .forms import wishesform

# Create your views here.
def home(request):
    return render (request, 'home.html')

def wish(request):
    if request.method == 'POST':
        wishes = wishesform(request.POST)
        if wishes.is_valid():
            wishes.save()
            print("Saved")
            return redirect('thankyou')
        else:
            print(wishes.errors)
    return render(request, 'form.html')

def thankyou(request):
    return render(request, 'thankyou.html')

