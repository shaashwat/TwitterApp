from django.shortcuts import render
from django.views.generic import TemplateView

from utils import getTweets

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        if request.method == "POST":
            screenname = request.POST.get("handle", None)
            result = getTweets.get_tweets(screenname)
            return render(request, 'result.html', {'result': result})
        return render(request, 'index.html', context=None)

# Create your views here.
