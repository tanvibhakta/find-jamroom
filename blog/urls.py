from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_search, name='home_search'),
    url(r'^list_all$', views.list_all, name='list_all'),
    url(r'^book$', views.book, name='book'),
    # url(r'^blog/search_result_display.html$', views.search_result_display, name='search_result_display'),
    # url(r'^result/$', home_search, name='home_search'),

]
