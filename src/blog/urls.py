from django.contrib import admin
from django.urls import path
from .views import index, blog, contact
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('contact/', contact)
]

urlpatterns += staticfiles_urlpatterns()
