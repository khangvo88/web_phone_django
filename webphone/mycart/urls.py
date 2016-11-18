from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexCartPage.as_view(), name='index'),
    url(r'^user/$', views.create_user,name='user-create'),
    url(r'^login/$', views.login_page,name='login'),
]