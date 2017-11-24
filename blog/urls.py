from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_search, name='home_search'),
    # url(r'^result/$', home_search, name='home_search'),

]
