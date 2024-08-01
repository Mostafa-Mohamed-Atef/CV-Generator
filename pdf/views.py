from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def home(request):
    return render(request, 'pdf/base.html')


#still doesn't work fix it tomorrow 
def submit(request):
    form = ProfileForm(request.POST or None)
    if request.method == "POST":
        name = request.POST.get("name","")
        profile = Profile(name=name)
        form.save()
    return render(request, "pdf/done.html", {"form":form})