from django.conf.urls import url
from formExample import views

urlpatterns = [
    url(r'^forms$',views.formexample)
]