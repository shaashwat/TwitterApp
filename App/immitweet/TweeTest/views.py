from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


from utils import getTweets

# Create your views here.

# Current view to display the index html site. If it recognizes a POST request, it will display the result as plain text.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if request.method == "POST":
            screenname = request.POST.get("handle", None)
            result = getTweets.get_tweets(screenname)
            return HttpResponse(result, content_type="text/plain")
        return render(request, 'index.html', context=None)


class ResultPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'result.html', context=None)
# Create your views here.
