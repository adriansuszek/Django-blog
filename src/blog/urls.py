from django.contrib import admin
from django.urls import path
from posts.views import index, blog, contact #PAMIETAJMY, ZE VIEWS IMPORTUJE Z apki - posts!!!
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog),
    path('contact/', contact)
]

# urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
