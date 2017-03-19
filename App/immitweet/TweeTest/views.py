from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


from utils import getTweets

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


def viewTweets(self,request):
    if request.method == "POST":
        screenname = request.POST.get("handle", None)
        result = getTweets.get_tweets(screenname)
        return HttpResponse(result, content_type="text/plain")
    elif request.method == "GET":
        return HttpResponse("Hello", content_type="text/plain")

class ResultPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'result.html', context=None)
# Create your views here.
#hi