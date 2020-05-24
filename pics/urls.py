from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns=[
    path('',views.index, name = 'indexPage'),
    path('search/',views.search_results, name='search_results'),
    path('category/',views.search_location, name='category'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)