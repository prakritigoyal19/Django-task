from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'final', views.calculations, name="calculations"),
    url(r'^$', views.data, name="data"),
]