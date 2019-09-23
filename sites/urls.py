from django.conf.urls import url
from sites import views

urlpatterns = [
    url(r'^signup$',views.userRegistration, name = 'signup'),
    url(r'^login$',views.userLogin, name = 'login'),
    url(r'^dashboard$', views.userDashboard, name ='dashboard'),
    url(r'^logout', views.userLogout, name ='logout'),
    url(r'^forgot_password$', views.forgotPassword, name='forgot_password'),
    url(r'^static_example$', views.staticExamples , name ='static_example'),

]