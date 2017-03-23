from django.conf.urls import url
from TweeTest import views

urlpatterns = [
    url(r'^$', views.view_home, name='home'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),
    url(r'^result/$', views.ResultPageView.as_view()),

]

