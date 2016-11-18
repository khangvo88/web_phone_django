from django.conf.urls import url, handler404
from . import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = views.page_not_found


urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    #url(r'^(?P<smartphone_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product-detail'), #change smartphone_id to <pk>
    url(r'^p/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='producer'), #change smartphone_id to <pk>
    url(r'^(?P<smartphone_id>[0-9]+)/buy/$', views.buy, name='buy'),    
    url(r'^name/$', views.get_name, name='name'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^upload/$', views.upload_file, name='upload'),
    url(r'^c/(?P<category_id>[0-9]+)$', views.IndexView.as_view(), name='category'), # FIXME: update model view
]