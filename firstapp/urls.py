# from django.conf.urls import url
# from firstapp import views
# from django.urls import path, include
# from django.conf.urls.static import static
# from django.views.generic import TemplateView
# from django.conf import settings
# from django.contrib import admin
# from project1 import urls
# urlpatterns = [

#     # path('',views.index,name='index'),
#     path('', include('project1.urls')),
#     path('hostels/', include('project1.urls')),
#     path('gents/', include('project1.urls')),
#     path('ladies', include('project1.urls'))


# ]
from django.conf import settings
from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.hostels, name='hostels'),
    path('gents/', views.gents, name='gents'),
    path('ladies/', views.ladies, name='ladies'),
    path('moreinfo/', views.moreinfo, name='moreinfo'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
