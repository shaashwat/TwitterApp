from django.conf.urls import url
from TweeTest import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
