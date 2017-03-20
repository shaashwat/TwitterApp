from django.shortcuts import render
from django.http import HttpResponse


from utils import getTweets

# Create your views here.

# Current view to display the index html site. If it recognizes a POST request, it will display the result as plain text.
def view_name(request):
    if request.method == "POST":
        screenname = request.POST.get("handle", None)
        result = getTweets.get_tweets(screenname)
        return HttpResponse(result, content_type="text/plain")
    return render(request, 'index.html', {})

# Create your views here.
