from django.conf.urls import url
from TweeTest import views

urlpatterns = [
    url(r'^$', views.view_name, name='home'),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^contact/$', views.ContactPageView.as_view()),

]

