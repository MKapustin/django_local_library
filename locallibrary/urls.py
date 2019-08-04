from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^register/$', views.RegisterFormView.as_view(), name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
