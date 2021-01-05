from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login_page, name = 'login'),
    path('register', views.register_page, name = 'register'),
    path('logout', views.logout, name = 'logout')
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
