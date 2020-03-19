from django.contrib import admin
from django.urls import path
from .views import index, blog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog)
]

urlpatterns += staticfiles_urlpatterns()
