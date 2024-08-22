from django.shortcuts import render
from .models import Subscribers

# Create your views here.
def home(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribers = Subscribers.objects.create(email=email)

        return render(request, 'success.html')
    return render(request, 'coming_soon.html')