from django.conf.urls import url
from testApp import views

urlpatterns = [
    url(r'^hello$',views.hellodjango, name = 'hello_django'),
    url(r'^welcome$',views.welcomedjango, name= 'welcome_django')

]