from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),  # Correctly includes movies/urls.py
    path('', RedirectView.as_view(url='/movies/', permanent=True)),
]
