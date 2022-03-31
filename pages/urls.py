from django.urls import path
from .views import homePageView, readfile, writetofile

urlpatterns = [
    path("", homePageView, name="home"),
    path("readfile", readfile),
    path("filewrite", writetofile)
]
