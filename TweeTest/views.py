from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import Context, loader

from utils import runThis

# Create your views here.

# Current view to display the index html site. If it recognizes a POST request, it will display the result as plain text.
def view_home(request):
    if request.method == "POST":
        screenname = request.POST.get("handle", None)
        result = runThis.getTweets(screenname).decode('utf-8')
        page = loader.get_template("result.html")

        return render(request,'result.html',{"result":result, "screenname":screenname})

    return render(request, 'index.html', {})

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class ResultPageView(TemplateView):
    template_name = "result.html"


# Create your views here.
