from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.views.generic import CreateView
# Create your views here.
def home(request):
    return render(request, 'pdf/base.html')


#still doesn't work fix it tomorrow 
def adding(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('done')
    return render(request, "pdf/adding.html", {"form":form})
    