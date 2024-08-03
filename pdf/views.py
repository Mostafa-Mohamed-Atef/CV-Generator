from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.views.generic import CreateView
import pdfkit 
from django.http import HttpResponse
from django.template import loader 
# Create your views here.
def home(request):
    return render(request, 'pdf/base.html')


#still doesn't work fix it tomorrow 
def adding(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "pdf/adding.html", {"form":form})

def cv(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({"user_profile":user_profile})
    options = {
        "page-size":'letter',
        "encoding":"UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options) #for turning html to pdf 
    response = HttpResponse(pdf, content_type="application/pdf")
    response["content-Disposition"]="attachment"
    filename="cv.pdf"
    return response

def list(request):
    profile = Profile.objects.all()
    return render(request, 'pdf/list.html', {"profile":profile})