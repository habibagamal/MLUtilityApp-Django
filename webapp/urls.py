from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^form', views.form, name="form")
#    url(r'^submit', views.submit, name = "submit")
               
]
