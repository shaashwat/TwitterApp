from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from utils import runThis

# Create your views here.

# Current view to display the index html site. If it recognizes a POST request, it will display the result as plain text.
def view_home(request):
    if request.method == "POST":
        screenname = request.POST.get("handle", None)
        result = runThis.getTweets(screenname)
        return HttpResponse(result, content_type="text/plain")
    return render(request, 'index.html', {})

def view_tweet(request):
    return render(request,'result.html')

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"



# Create your views here.
