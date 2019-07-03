from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/report/', include('report.api.urls')),
    path('', home, name='home')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]