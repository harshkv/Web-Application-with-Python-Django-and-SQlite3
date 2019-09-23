from django.conf.urls import url
from crud import views


urlpatterns = [
    url(r'^create$', views.create, name='create'),
    url(r'^index$', views.index, name='index'),
    url(r'^update/(?P<id>[0-9]+)$', views.update, name='update'),
    url(r'^view/(?P<id>[0-9]+)$', views.view, name='view'),
    url(r'^delete/(?P<id>[0-9]+)$', views.delete, name='delete'),
    url(r'^educreate$', views.edu_Create, name='eduCreate'),
    url(r'^eduindex$', views.edu_Index, name='eduIndex'),
    url(r'^eduupdate/(?P<id>[0-9]+)$', views.edu_Update, name='eduupdate'),
    url(r'^edudelete/(?P<id>[0-9]+)$', views.edu_Delete, name='edudelete'),
    url(r'^eduview/(?P<id>[0-9]+)$', views.edu_View, name='eduview'),
    url(r'^create_View$', views.CreateView.as_view(), name ="create_view"),
    # url(r'^load_data$', views.load_data, name="load_data"),

]