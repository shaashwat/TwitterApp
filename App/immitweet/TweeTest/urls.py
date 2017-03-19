from django.conf.urls import url
from TweeTest import views

urlpatterns = [
    url(r'^$', views.view_name, name='home'),
]

