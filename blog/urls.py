from django.contrib import admin
from django.urls import path, include
from posts.views import index, blog, post, last_post, contact #PAMIETAJMY, ZE VIEWS IMPORTUJE Z apki - posts!!!
#mogloby by rowniez from post import views, i wtedy w urlpatterns:     path('blog/', views.blog, name='post-list'),
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('post/<slug:slug>/', post, name='post-detail'),
    path('post/', last_post),
    path('contact/', contact),
    # path('ckeditor/', include('ckeditor_uploader.urls'))
]

# urlpatterns += staticfiles_urlpatterns()

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print("urlpatterns: ", urlpatterns)
