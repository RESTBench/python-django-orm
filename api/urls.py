from django.conf.urls import url

from contact import views

urlpatterns = [
    url(r'^contact/$', views.ContactList.as_view()),
]
